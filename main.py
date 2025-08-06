import pandas as pd

# Load the Excel file with the correct extension
df = pd.read_excel("Online Retail.xlsx")

# Show the first 5 rows
print(df.head())

# Drop rows with missing CustomerID
df = df.dropna(subset=['CustomerID'])

# Remove transactions with negative or 0 quantity
df = df[df['Quantity'] > 0]

# Create a TotalPrice column
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

# Preview cleaned data
print("Cleaned Data Preview:")
print(df.head())

import datetime as dt

# Set a reference date (1 day after the last purchase)
reference_date = df['InvoiceDate'].max() + dt.timedelta(days=1)

print("Reference date for Recency calculation:", reference_date)

# Calculate RFM metrics for each customer
rfm = df.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (reference_date - x.max()).days,  # Recency
    'InvoiceNo': 'nunique',                                   # Frequency
    'TotalPrice': 'sum'                                       # Monetary
})

# Rename columns for clarity
rfm.columns = ['Recency', 'Frequency', 'Monetary']

# Preview RFM table
print("\nRFM Table Preview:")
print(rfm.head())

# Assign scores from 1 to 5 for each metric
# Recency (usually descending order, higher score for recent)
rfm['R_Score'] = pd.qcut(rfm['Recency'], 5, labels=range(5, 0, -1), duplicates='drop')

# Frequency
freq_bins = pd.qcut(rfm['Frequency'], 5, duplicates='drop')
num_freq_bins = freq_bins.cat.categories.size
rfm['F_Score'] = pd.qcut(rfm['Frequency'], 5, labels=range(1, num_freq_bins + 1), duplicates='drop')

# Monetary
mon_bins = pd.qcut(rfm['Monetary'], 5, duplicates='drop')
num_mon_bins = mon_bins.cat.categories.size
rfm['M_Score'] = pd.qcut(rfm['Monetary'], 5, labels=range(1, num_mon_bins + 1), duplicates='drop')


# Preview scored RFM table
print("\nRFM Scored Table Preview:")
print(rfm.head())

# Combine RFM scores into a single string (e.g., 555, 123)
rfm['RFM_Score'] = rfm['R_Score'].astype(str) + rfm['F_Score'].astype(str) + rfm['M_Score'].astype(str)

# Define segmentation function
def segment_customer(row):
    if row['R_Score'] >= 4 and row['F_Score'] >= 4 and row['M_Score'] >= 4:
        return 'Best Customers'
    elif row['R_Score'] >= 3 and row['F_Score'] >= 3:
        return 'Loyal Customers'
    elif row['R_Score'] <= 2:
        return 'At Risk'
    else:
        return 'Others'

# Apply segmentation
rfm['Segment'] = rfm.apply(segment_customer, axis=1)

# Preview scored RFM table with segments
print("\nRFM Scored Table Preview:")
print(rfm.head())

print("\nRFM Table with Customer Segments:")
print(rfm[['RFM_Score', 'Segment']].head())

rfm.to_csv("rfm_customer_segments.csv")
