import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('wc.csv')

department_reviews = data['Department Name'].value_counts()

plt.figure(figsize=(10, 6))
department_reviews.plot(kind='bar', color='skyblue')
plt.title('Number of Reviews per Department')
plt.xlabel('Department')
plt.ylabel('Number of Reviews')
plt.xticks(rotation=45)
plt.tight_layout()


plt.savefig('vis.png')

