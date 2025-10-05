📊 Customer Segmentation Analysis
A comprehensive RFM (Recency, Frequency, Monetary) analysis and customer segmentation project for e-commerce data.

🎯 Project Overview
This project analyzes customer transaction data to segment customers into meaningful groups based on their purchasing behavior. The analysis helps businesses understand their customer base and develop targeted marketing strategies.

📈 Key Features
Data Cleaning & Preprocessing: Handled missing values, removed duplicates, and cleaned 540K+ transactions
RFM Analysis: Calculated Recency, Frequency, and Monetary metrics for 4,000+ customers
Customer Segmentation: Classified customers into 10 distinct segments (Champions, Loyal, At Risk, etc.)
Interactive Dashboard: Built a web-based dashboard for exploring insights
Visualizations: Created 15+ professional charts and graphs
🛠️ Technologies Used
Python 3.x
Pandas & NumPy: Data manipulation and analysis
Matplotlib & Seaborn: Static visualizations
Plotly: Interactive visualizations
Streamlit: Web dashboard
Jupyter Notebook: Development environment
📊 Customer Segments Identified
Champions 🏆 - Best customers with high RFM scores
Loyal Customers 💎 - Regular buyers with high value
Potential Loyalists 🌟 - Recent frequent buyers
New Customers 🆕 - Recent first-time buyers
Promising 📈 - Recent buyers with potential
Need Attention ⚠️ - Above average but decreasing activity
At Risk 🚨 - Used to be frequent, now declining
Cannot Lose Them 💔 - High value but inactive
Hibernating 😴 - Long time since purchase
Lost 👋 - Lowest engagement
📁 Project Structure
customer-segmentation/
│
├── data/
│   ├── Online Retail.xlsx           # Raw dataset
│   ├── cleaned_online_retail.csv    # Cleaned data
│   └── rfm_analysis.csv             # RFM results
│
├── images/                          # Visualizations
│   ├── segment_distribution.png
│   ├── rfm_heatmap.png
│   ├── rfm_distributions.png
│   ├── top_customers.png
│   ├── segment_revenue.png
│   └── rfm_3d_scatter.png
│
├── notebooks/
│   └── analysis.ipynb               # Jupyter notebook with analysis
│
├── dashboard.py                     # Streamlit dashboard
└── README.md                        # Project documentation
🚀 How to Run
Prerequisites
bash
pip install pandas numpy matplotlib seaborn scikit-learn plotly streamlit openpyxl
Running the Analysis
Open analysis.ipynb in Jupyter Notebook
Run all cells sequentially
Running the Dashboard
bash
streamlit run dashboard.py
The dashboard will open automatically in your browser at http://localhost:8501

📊 Key Insights
Top Revenue Segment: [Your top segment] contributes X% of total revenue
Customer Distribution: X% are Champions/Loyal, Y% need attention
Average Customer Value: $X per customer
Purchase Frequency: Average X orders per customer
💡 Business Recommendations
Champions & Loyal Customers
Implement VIP loyalty programs
Offer exclusive early access to new products
Personalized thank-you communications
At Risk & Cannot Lose Them
Urgent re-engagement campaigns
Special win-back offers
Survey to understand concerns
New & Promising Customers
Welcome email series
Educational content about products
First-purchase incentives
Hibernating & Lost
Minimal investment
Low-cost reactivation campaigns
Understand reasons for churn
📈 Results
Processed 540,000+ transactions
Analyzed 4,300+ unique customers
Identified 10 distinct customer segments
Created 15+ visualizations
Built interactive dashboard with 20+ metrics
📚 Data Source
UCI Machine Learning Repository - Online Retail Dataset

Dataset contains transactions from 2010-2011
UK-based online retail company
540,000+ records across 8 columns
👤 Author
[Your Name]

LinkedIn: [Your LinkedIn]
Email: [Your Email]
Portfolio: [Your Website]
📝 License
This project is open source and available for educational purposes.

🙏 Acknowledgments
UCI Machine Learning Repository for the dataset
Streamlit for the dashboard framework
Python data science community
