# GmE 221 - Laboratory Exercise 4: Spatial Statistics Autocorrelation and Cluster Detection
## Overview

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