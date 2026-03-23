import matplotlib.pyplot as plt

def visualize_neighbors(gdf, weights_obj):
    fig, ax = plt.subplots(figsize=(10,8))
    gdf.plot(ax=ax, color="lightblue", edgecolor="black")
    centroids = gdf.geometry.centroid
    
    ax.scatter(
        centroids.x,
        centroids.y,
        color="red",
        s=10,
        label="Parcel Centroids"
    )
    
    for i, neighbors in weights_obj.neighbors.items():
        x1 = centroids.iloc[i].x
        y1 = centroids.iloc[i].y
        
        for j in neighbors:
            x2 = centroids.iloc[j].x
            y2 = centroids.iloc[j].y
            
            ax.plot(
                [x1,x2],
                [y1, y2],
                color="green",
                alpha=0.4
            )

    plt.title("Spatial Weights Graph")
    plt.legend()
    plt.show()
    
def visualize_local_moran(gdf):
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(10, 8))

    colors = {
        "Hotspot": "red",
        "Coldspot": "blue",
        "Not Significant": "lightgrey"
    }

    for cluster, color in colors.items():
        subset = gdf[gdf["cluster"] == cluster]
        if not subset.empty:
            subset.plot(
                ax=ax,
                color=color,
                edgecolor="black",
                linewidth=0.2,
                label=cluster
            )
            
    plt.title("Local Moran's I Cluster Map")
    plt.legend()
    plt.tight_layout()
    plt.show()