import numpy as np

# Data
X = np.array([10, 12, 14, 40, 42, 45])

# Number of clusters
K = 2

# Starting centroids
start_c1 = 10
start_c2 = 40

c1 = start_c1
c2 = start_c2

# Run K-Means
for i in range(3):
    cluster1 = []
    cluster2 = []

    for x in X:
        if abs(x - c1) < abs(x - c2):
            cluster1.append(int(x))
        else:
            cluster2.append(int(x))

    c1 = sum(cluster1) / len(cluster1)
    c2 = sum(cluster2) / len(cluster2)

# Final Output
print("Starting Centroids:")
print("C1 =", start_c1)
print("C2 =", start_c2)

print("\nFinal Centroids:")
print("C1 =", c1)
print("C2 =", c2)

print("\nCluster Data:")
print("Cluster 1:", cluster1)
print("Cluster 2:", cluster2)
