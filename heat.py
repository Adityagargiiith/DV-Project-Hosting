import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file into a DataFrame
df = pd.read_csv('startups2.csv')

# Convert 'Date Joined' column to datetime
df['Date Joined'] = pd.to_datetime(df['Date Joined'])

# Extract the year and create 'Year Joined' column
df['Year Joined'] = df['Date Joined'].dt.year

# Group by 'Industry' and 'Year Joined' and count the number of companies
heatmap_data = df.groupby(['Industry', 'Year Joined']).size().reset_index(name='Count')

# Pivot the data to create a matrix suitable for heatmap
heatmap_matrix = heatmap_data.pivot(index='Industry', columns='Year Joined', values='Count')

# Create the heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(heatmap_matrix, cmap='YlGnBu', annot=True, fmt='g', linewidths=.5)
plt.title('Number of Companies by Industry and Year Joined')
plt.xlabel('Year Joined')
plt.ylabel('Industry')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('heatmap.png')
plt.show()
