"""
This script visualizes the results of the RFM analysis by generating two key plots:

1. A heatmap that shows the average monetary value of customers based on their Recency and Frequency scores.
   This helps identify which customer groups spend the most money.

2. A bar chart that displays the number of customers in each segment (e.g., Best Customers, Loyal Customers, At Risk).
   This gives an overview of customer distribution across segments.

The script reads the preprocessed RFM data from 'rfm_customer_segments.csv' and creates insightful visualizations
to aid in business decisions and marketing strategies.
"""
# Import necessary libraries for visualization
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the RFM CSV file
rfm = pd.read_csv("rfm_customer_segments.csv")

# Convert R, F, M scores to integers
# Sometimes when reading from CSV, numeric scores are read as strings
# Converting them back to integers ensures proper sorting and plotting
rfm['R_Score'] = rfm['R_Score'].astype(int)
rfm['F_Score'] = rfm['F_Score'].astype(int)
rfm['M_Score'] = rfm['M_Score'].astype(int)

# --- Create a heatmap showing average Monetary value by Recency and Frequency scores ---
# We create a pivot table where rows are Recency scores and columns are Frequency scores
# The cell values represent the average Monetary value for that R-F combination
pivot_table = rfm.pivot_table(index='R_Score', columns='F_Score', values='Monetary', aggfunc='mean')

plt.figure(figsize=(8,6))
# Plot heatmap with annotations of the average monetary values
sns.heatmap(pivot_table, annot=True, fmt=".0f", cmap='YlGnBu')
plt.title('Heatmap of Avg. Monetary Value by Recency and Frequency')
plt.xlabel('Frequency Score')
plt.ylabel('Recency Score')
# Invert y-axis so higher Recency scores appear at the top (more recent customers)
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

# --- Create a bar chart showing the number of customers in each segment ---
plt.figure(figsize=(8,5))
# Countplot shows how many customers fall into each segment category
# The order is set so segments with more customers appear first
sns.countplot(data=rfm, x='Segment', order=rfm['Segment'].value_counts().index)
plt.title('Number of Customers by Segment')
plt.xlabel('Customer Segment')
plt.ylabel('Count')
# Rotate x-axis labels slightly for better readability
plt.xticks(rotation=20)
plt.tight_layout()
plt.show()
