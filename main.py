"""
This script performs RFM (Recency, Frequency, Monetary) analysis on the Online Retail dataset
to segment customers based on their purchasing behavior.

Steps included:
- Load and clean the raw transaction data (remove invalid or missing entries)
- Calculate Recency, Frequency, and Monetary values for each customer
- Score each metric on a scale from 1 to 5
- Combine these scores to create an overall RFM score
- Segment customers into groups such as 'Best Customers', 'Loyal Customers', and 'At Risk'

The output is saved as 'rfm_customer_segments.csv', which contains customer scores and segments,
useful for targeted marketing and business decision-making.
"""

# Import pandas library for data manipulation
import pandas as pd

# Load the Excel file with the correct extension
df = pd.read_excel("Online Retail.xlsx")

# Show the first 5 rows
print(df.head())

# Remove rows where 'CustomerID' is missing (important for customer analysis)
df = df.dropna(subset=['CustomerID'])

# Remove transactions where quantity is zero or negative (these might be returns or errors)
df = df[df['Quantity'] > 0]

# Add a new column 'TotalPrice' to calculate total spent per transaction (Quantity * UnitPrice)
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

# Preview cleaned data to check changes after cleaning
print("Cleaned Data Preview:")
print(df.head())

# Import datetime for date calculations
import datetime as dt

# Define a 'reference date' as one day after the most recent purchase date in the dataset
# This will be used to calculate Recency (how recent was the last purchase)
reference_date = df['InvoiceDate'].max() + dt.timedelta(days=1)

print("Reference date for Recency calculation:", reference_date)

# Group data by CustomerID and calculate RFM metrics:
# Recency: days since last purchase (difference between reference_date and customer's last purchase)
# Frequency: total number of unique invoices (purchase events) per customer
# Monetary: total amount spent by the customer
rfm = df.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (reference_date - x.max()).days,  # Recency
    'InvoiceNo': 'nunique',                                   # Frequency
    'TotalPrice': 'sum'                                       # Monetary
})

# Rename the aggregated columns to meaningful names
rfm.columns = ['Recency', 'Frequency', 'Monetary']

# Preview RFM table
print("\nRFM Table Preview:")
print(rfm.head())

# Assign scores from 1 to 5 for each metric
# Recency (usually descending order, higher score for recent)
rfm['R_Score'] = pd.qcut(rfm['Recency'], 5, labels=range(5, 0, -1), duplicates='drop')

# Frequency: higher frequency means more loyal customer, so higher score for higher frequency
freq_bins = pd.qcut(rfm['Frequency'], 5, duplicates='drop')
num_freq_bins = freq_bins.cat.categories.size
rfm['F_Score'] = pd.qcut(rfm['Frequency'], 5, labels=range(1, num_freq_bins + 1), duplicates='drop')

# Monetary: higher spending means higher score
mon_bins = pd.qcut(rfm['Monetary'], 5, duplicates='drop')
num_mon_bins = mon_bins.cat.categories.size
rfm['M_Score'] = pd.qcut(rfm['Monetary'], 5, labels=range(1, num_mon_bins + 1), duplicates='drop')


# Preview scored RFM table
print("\nRFM Scored Table Preview:")
print(rfm.head())

# Combine RFM scores into a single string (e.g., 555, 123)
rfm['RFM_Score'] = rfm['R_Score'].astype(str) + rfm['F_Score'].astype(str) + rfm['M_Score'].astype(str)

# Define a function to assign each customer to a segment based on their RFM scores
def segment_customer(row):
    if row['R_Score'] >= 4 and row['F_Score'] >= 4 and row['M_Score'] >= 4:
        return 'Best Customers'
    elif row['R_Score'] >= 3 and row['F_Score'] >= 3:
        return 'Loyal Customers'
    elif row['R_Score'] <= 2:
        return 'At Risk'
    else:
        return 'Others'

# Apply the segmentation function to each row of the RFM table
rfm['Segment'] = rfm.apply(segment_customer, axis=1)

# Preview scored RFM table with segments
print("\nRFM Scored Table Preview:")
print(rfm.head())

print("\nRFM Table with Customer Segments:")
print(rfm[['RFM_Score', 'Segment']].head())

# Save the final RFM table with segments to a CSV file for future use or visualization
rfm.to_csv("rfm_customer_segments.csv")
