import pandas as pd
from sklearn.cluster import KMeans

# Load the preprocessed DataFrame (replace 'file_path' with your file path)
data = pd.read_csv('wc.csv')

# Select columns suitable for K-means
selected_columns = ['Age', 'Rating']

# Fit K-means algorithm with k=3
kmeans = KMeans(n_clusters=3, random_state=42)
data['cluster'] = kmeans.fit_predict(data[selected_columns])

# Count the number of records in each cluster
cluster_counts = data['cluster'].value_counts()

# Save the cluster counts to a text file 'k.txt'
cluster_counts.to_csv('k.txt', header=False)
