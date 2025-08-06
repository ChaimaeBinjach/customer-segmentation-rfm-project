# 🛍️ Customer Segmentation Using RFM Analysis

This project applies **RFM (Recency, Frequency, Monetary) analysis** to segment customers based on their purchasing behavior using the popular **Online Retail Dataset**.  
The goal is to help businesses identify their best customers, re-engage inactive ones, and optimize marketing strategies.

---

## 📊 What Is RFM Analysis?

RFM stands for:

- **Recency**: How recently did the customer purchase?
- **Frequency**: How often do they purchase?
- **Monetary**: How much money did they spend?

We score customers from **1 (low)** to **5 (high)** on each of these metrics and segment them based on patterns in their scores.

---

## 📁 Dataset Used

- **Source**: [UCI Machine Learning Repository – Online Retail Dataset](https://archive.ics.uci.edu/ml/datasets/online+retail)
- **Description**: Transactions from a UK-based online retailer from **Dec 2010 to Dec 2011**
- **File Name**: `Online Retail.xlsx`

---

## ⚙️ Tools & Libraries Used

This project uses **Python** and the following libraries:

| Library         | Purpose                                                                 |
|----------------|-------------------------------------------------------------------------|
| `pandas`        | For loading, cleaning, and analyzing the dataset                       |
| `matplotlib`    | For creating bar charts and visualizations                             |
| `seaborn`       | For making heatmaps and enhancing chart aesthetics                     |
| `openpyxl`      | Allows reading Excel `.xlsx` files with `pandas.read_excel()`          |


---

## 🧠 Step-by-Step Solution Approach

1. **Understand the Goal**  
   Segment customers by behavior to personalize marketing.

2. **Clean the Data**  
   - Drop missing customer IDs  
   - Remove returns/invalid rows (negative quantity)  
   - Add `TotalPrice = Quantity * UnitPrice`

3. **Calculate RFM Metrics**  
   For each customer:
   - `Recency`: Days since their last purchase
   - `Frequency`: Number of unique invoices
   - `Monetary`: Total amount spent

4. **Score Each Metric**  
   - Use `qcut()` to assign scores from **1 to 5** (higher is better)
   - Create `RFM_Score` like `555`, `431`, etc.

5. **Segment the Customers**  
   Using logical rules:
   - Best Customers: High R, F, M
   - Loyal Customers: High F and moderate R
   - At Risk: Low R
   - Others: Remaining users

6. **Visualize the Results**  
   - Heatmap: Avg. Monetary by Recency & Frequency
   - Bar Chart: Count of customers in each segment

---

📁 customer-segmentation-rfm-project/
  - main.py                    # Data cleaning + RFM scoring + segmentation
  - visualize_rfm.py           # Heatmap & bar chart for segment visualization
  - Online Retail.xlsx         # Original dataset
  - rfm_customer_segments.csv  # Final output (RFM + segment info)
  - README.md                  # Project documentation (this file)


---

## 🔍 File Descriptions

### 📄 `main.py`

- Loads and cleans the dataset  
- Calculates Recency, Frequency, and Monetary values  
- Scores customers on each RFM dimension (1–5)  
- Creates the final RFM table and segments  
- Saves output to `rfm_customer_segments.csv`

### 📄 `visualize_rfm.py`

- Loads the RFM CSV file  
- Creates:
  - 🔥 **Heatmap** of Monetary values by Recency & Frequency  
  - 📊 **Bar Chart** of customer segment counts

---

## 🧠 Segmentation Logic

| Segment            | Condition                         |
|--------------------|------------------------------------|
| **Best Customers** | R, F, M scores all ≥ 4             |
| **Loyal Customers**| R ≥ 3 and F ≥ 3                    |
| **At Risk**        | R ≤ 2                              |
| **Others**         | Remaining customers                |

---

## 💡 Marketing Strategy Suggestions

| Segment            | Strategy                                         |
|--------------------|--------------------------------------------------|
| **Best Customers** | Exclusive VIP perks, early access to new launches |
| **Loyal Customers**| Loyalty rewards, referral bonuses                |
| **At Risk**        | Win-back emails, special discounts               |
| **Others**         | Newsletter campaigns, new product teasers        |

---
---

## 🙋‍♀️ Author

Made with 💻 and ☕ by [Chaimae Binjach](https://github.com/ChaimaeBinjach)  
Feel free to ⭐ the repo or contribute!


