# GmE 221 - Laboratory Exercise 4: Spatial Statistics Autocorrelation and Cluster Detection
## Overview
The focus of this laboratory is to evaluate spatial autocorrelation in parcel‑level valuation data using both Global Moran’s I and Local Moran’s I. The analysis is performed entirely in Python using GeoPandas, PySAL, Matplotlib, and SQLAlchemy, with PostGIS serving as the storage and retrieval environment for spatial data.

The workflow includes:
- Retrieving parcel geometries and valuation attributes from PostGIS
- Constructing spatial weights matrices (Contiguity, KNN, and Distance‑based)
- Computing Global Moran’s I to assess overall clustering
- Computing Local Moran’s I to identify hotspots, coldspots, and nonsignificant parcels
- Exporting cluster results to GeoJSON for QGIS visualization
- Visualizing spatial weights and local clusters using Matplotlib

The outputs of this analysis support understanding of how spatial processes and valuation patterns behave across the study area, providing insights into clustering behavior and the influence of neighborhood definitions.

---

## Environment Setup
- Python 3.14
- `PostgreSQL` with `PostGIS`
- `GeoPandas`, `SQLAlchemy`, `psycopg2-binary`, `libpysal`, `esda`, `NumPy`, `matplotlib`

---

## How to Run
1. Activate the virtual environment
2. Run `analysis.py`

---

## Reflection
### Visualizing Spatial Weights
The spatial weights graph helped me clearly see how neighborhood relationships are represented in my dataset. By plotting the parcel centroids as points and connecting them with lines, the graph effectively showed how each parcel is linked to its neighbors based on the chosen spatial weights. The centroids acted as nodes, and the connecting lines served as edges in a spatial network, making the abstract idea of spatial adjacency more understandable.

When I compared the three weighting methods `contiguity`, `KNN`, and `distance-based` I noticed clear differences in the structure of the neighbor graph. `Contiguity weights` created the most realistic representation, showing connections only between parcels that share actual boundaries. `KNN` produced a much denser and more uniform network, where each parcel was connected to a fixed number of nearest neighbors even if they were relatively far away. `Distance-based` weights varied depending on the threshold a small threshold generated sparse connections, but increasing it quickly created long-distance links and a very dense graph. These differences highlighted how each method interprets neighborhood differently.

Adjusting the parameters made the connectivity of the graph even more noticeable. Increasing `k` in the KNN method added more neighbor links per parcel, while increasing the distance threshold created larger clusters and more extensive reach between parcels. In both cases, the graph became more connected and visually busier, showing how parameter choices can easily shift the overall network density.

A denser spatial network generally strengthens the degree of spatial autocorrelation because parcels have more neighbors influencing them. This can either reveal stronger clustering or artificially inflate spatial dependence if the weight parameters are not chosen carefully. This is why selecting appropriate settings is important, especially when preparing for Moran’s I calculations.

For my dataset, `contiguity weights` best represent real spatial relationships because parcel influences are usually determined by shared boundaries rather than forced nearest-neighbor connections or arbitrary distance cutoffs. Contiguity reflects the true geometry and layout of land parcels, which makes it the most meaningful choice for parcel-level analysis.

Finally, visualizing spatial weights before running Moran’s I is essential because it allows me to verify whether the neighborhood structure actually matches the spatial characteristics of the area. If the weights are incorrect, too dense, too sparse, or connecting parcels that shouldn’t be neighbors the statistical results would be misleading. The visualization step helps prevent these analytical mistakes by ensuring the spatial weights are appropriate before moving on to spatial autocorrelation analysis.

### Global Autocorrelation
Computing Global Moran’s I allowed me to measure the overall spatial autocorrelation present in the parcel dataset. A positive Moran’s I indicates that similar values, such as high or low assessed values, tend to cluster together, while a value near zero suggests a more random pattern. The p‑value is essential because it tells me whether the observed pattern is statistically significant or could have occurred by chance. When comparing the two attributes `assessed value` and `market value` I noticed that each produced different Moran’s I results, which makes sense because these variables reflect different economic factors and therefore have different spatial behaviors. Moran’s I also depends on the spatial weights matrix, which defines how parcels are spatially related, and the attribute values themselves. Without a correct neighborhood definition, the autocorrelation results would be misleading because the measure relies on both spatial structure and attribute variation.

### Interpreting Local Spatial Autocorrelation
Computing `Local Moran’s I` allowed me to see how spatial clustering actually behaves across the study area. Unlike the global statistic, which only tells me whether clustering exists overall, the local analysis identified the exact parcels forming statistically significant `hotspots` and `coldspots`. Based on the resulting map, `hotspots` appear prominently in the central and southern sections of the subdivision, where many adjacent parcels show consistently high assessed values. These red clusters indicate areas where higher-value parcels reinforce each other spatially. In contrast, `coldspots` form a large, coherent block along the western boundary and smaller pockets on the eastern edge. These blue areas represent parcels where low values tend to cluster together. Meanwhile, most of the interior blocks, especially in the northern and middle neighborhoods, show no significant autocorrelation and remain classified as `Not Significant`.

The spatial pattern shown in the map highlights clear geographic differences across the area. The large coldspot zone on the left side suggests a lower-value cluster that is spatially consistent, possibly due to land use, development age, or parcel size. The hotspot zones, which dominate the central and southeastern portions, align with areas that appear to be more developed or systematically higher in value. The map also reveals some interesting transitions where hotspot clusters border nonsignificant zones, showing areas where parcel values shift between stronger and weaker spatial influence.

I also noticed how sensitive the results were to the spatial weights method used. With contiguity weights, the clusters aligned cleanly with the actual block and parcel boundaries, producing compact and realistic hotspot and coldspot shapes that match the subdivision layout. When experimenting with KNN or distance-based weights earlier, the clusters tended to stretch or connect across areas that did not share boundaries, which produced results that felt less natural for parcel-level data. This confirmed that contiguity weights were the most appropriate choice for this dataset, since parcel influence is best represented by shared boundaries rather than arbitrary distance cutoffs or fixed numbers of nearest neighbors.

The choice of attribute also plays an important role. The map shown reflects the spatial clustering of the assessed value attribute, and if I were to repeat the analysis for market value, I would expect the clusters to shift. These two value metrics represent different valuation processes, and Local Moran’s I helps highlight how their spatial distributions differ in real space. This reinforces that selecting the appropriate variable is just as important as selecting the correct spatial weights.

Finally, this part of the lab showed me why visualization is essential before interpreting any spatial statistical output. Seeing the clusters mapped out exposes possible issues such as overconnected weights, sparse neighborhoods, or unexpected patterns. Without the map, I might have misinterpreted the numeric results or overlooked spatial structures that only become obvious when visualized. The Local Moran’s I map makes it easier to understand the geographic meaning behind hotspots and coldspots, ensuring that the analysis reflects actual spatial processes rather than errors in configuration or assumptions.