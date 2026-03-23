import geopandas as gpd
from sqlalchemy import create_engine
from spatial_weights import contiguity_weights, knn_weights, distance_weights
from visualization import visualize_neighbors
from moran import calculate_global_morans_I
from esda.moran import Moran_Local
import os
from visualization import visualize_local_moran

# Database credentials
host = "localhost"
port = "5432"
dbname = "gme221_exer4"
user = "postgres"
password = "jivimigols8118"

conn_str = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}"

engine = create_engine(conn_str)

sql_query = """
SELECT gid, ass_ass_va, ass_market, geom
FROM public.assessed_parcels;
"""

gdf = gpd.read_postgis(sql_query, engine, geom_col="geom")

w = contiguity_weights(gdf)

# w = knn_weights(gdf, k=6)

# w = distance_weights(gdf, threshold=25)

# visualize_neighbors(gdf, w)

for attribute in ["ass_ass_va", "ass_market"]:
    moran_I, p_value = calculate_global_morans_I(gdf, w, attribute)
    print(f"Global Moran's I ({attribute}):, {moran_I:.4f}")
    print(f"p-value ({attribute}): {p_value:.4f}")

local = Moran_Local(gdf["ass_ass_va"], w)

gdf["local_I"] = local.Is
gdf["p_value"] = local.p_sim

alpha = 0.05
gdf["cluster"] = "Not Significant" 

gdf.loc[(gdf["local_I"] > 0) & (gdf["p_value"] < alpha), "cluster"] = "Hotspot" 
gdf.loc[(gdf["local_I"] < 0) & (gdf["p_value"] < alpha), "cluster"] = "Coldspot" 

os.makedirs("output", exist_ok=True) 

gdf.to_file( 
            "output/spatial_clusters.geojson", 
            driver="GeoJSON" 
) 

print("Saved: output/spatial_clusters.geojson")

visualize_local_moran(gdf)