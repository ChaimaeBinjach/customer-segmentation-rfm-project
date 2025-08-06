import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the RFM CSV file
rfm = pd.read_csv("rfm_customer_segments.csv")

# Convert scores to integers (in case they're read as strings)
rfm['R_Score'] = rfm['R_Score'].astype(int)
rfm['F_Score'] = rfm['F_Score'].astype(int)
rfm['M_Score'] = rfm['M_Score'].astype(int)

# --- Heatmap: Monetary value by Recency & Frequency ---
pivot_table = rfm.pivot_table(index='R_Score', columns='F_Score', values='Monetary', aggfunc='mean')

plt.figure(figsize=(8,6))
sns.heatmap(pivot_table, annot=True, fmt=".0f", cmap='YlGnBu')
plt.title('Heatmap of Avg. Monetary Value by Recency and Frequency')
plt.xlabel('Frequency Score')
plt.ylabel('Recency Score')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

# --- Bar Chart: Customer count per segment ---
plt.figure(figsize=(8,5))
sns.countplot(data=rfm, x='Segment', order=rfm['Segment'].value_counts().index)
plt.title('Number of Customers by Segment')
plt.xlabel('Customer Segment')
plt.ylabel('Count')
plt.xticks(rotation=20)
plt.tight_layout()
plt.show()
