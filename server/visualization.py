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