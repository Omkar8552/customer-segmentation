import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Page configuration
st.set_page_config(
    page_title="Customer Segmentation Dashboard",
    page_icon="📊",
    layout="wide"
)

# Title and description
st.title("📊 Customer Segmentation Analysis Dashboard")
st.markdown("### RFM-Based Customer Segmentation for E-Commerce")
st.markdown("---")

# Load data with better error handling
@st.cache_data
def load_data():
    try:
        # Load RFM data
        rfm = pd.read_csv('data/rfm_analysis.csv')
        
        # Check if first column is unnamed (it's the index)
        if rfm.columns[0] in ['Unnamed: 0', 'index']:
            rfm.rename(columns={rfm.columns[0]: 'CustomerID'}, inplace=True)
        
        # If CustomerID is not in columns, it means it's the index
        if 'CustomerID' not in rfm.columns:
            rfm = rfm.reset_index()
            if 'index' in rfm.columns:
                rfm.rename(columns={'index': 'CustomerID'}, inplace=True)
        
        # Load transaction data
        df = pd.read_csv('data/cleaned_online_retail.csv')
        df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
        
        return rfm, df
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return None, None

rfm, df = load_data()

if rfm is not None and df is not None:
    
    # Debug info (you can remove this later)
    with st.expander("🔍 Debug Info - Column Names"):
        st.write("RFM Columns:", rfm.columns.tolist())
        st.write("RFM Shape:", rfm.shape)
        st.write("First row:", rfm.head(1))
    
    # Sidebar filters
    st.sidebar.header("🔍 Filters")
    
    # Check if Customer_Segment column exists
    if 'Customer_Segment' in rfm.columns:
        segments = ['All'] + list(rfm['Customer_Segment'].unique())
        selected_segment = st.sidebar.selectbox("Select Customer Segment", segments)
        
        # Filter data based on selection
        if selected_segment != 'All':
            rfm_filtered = rfm[rfm['Customer_Segment'] == selected_segment]
        else:
            rfm_filtered = rfm
    else:
        st.warning("Customer_Segment column not found. Showing all data.")
        rfm_filtered = rfm
        selected_segment = 'All'
    
    # Key Metrics (Top of dashboard)
    st.header("📈 Key Metrics")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Customers", f"{len(rfm_filtered):,}")
    with col2:
        if 'Recency' in rfm_filtered.columns:
            st.metric("Avg Recency (Days)", f"{rfm_filtered['Recency'].mean():.1f}")
        else:
            st.metric("Avg Recency", "N/A")
    with col3:
        if 'Frequency' in rfm_filtered.columns:
            st.metric("Avg Frequency", f"{rfm_filtered['Frequency'].mean():.1f}")
        else:
            st.metric("Avg Frequency", "N/A")
    with col4:
        if 'Monetary' in rfm_filtered.columns:
            st.metric("Total Revenue", f"${rfm_filtered['Monetary'].sum():,.2f}")
        else:
            st.metric("Total Revenue", "N/A")
    
    st.markdown("---")
    
    # Row 1: Segment Distribution
    if 'Customer_Segment' in rfm.columns:
        st.header("👥 Customer Segment Distribution")
        col1, col2 = st.columns(2)
        
        with col1:
            # Bar chart
            segment_counts = rfm['Customer_Segment'].value_counts().reset_index()
            segment_counts.columns = ['Segment', 'Count']
            
            fig1 = px.bar(segment_counts, x='Segment', y='Count',
                         title='Customer Count by Segment',
                         color='Count',
                         color_continuous_scale='Viridis')
            fig1.update_layout(xaxis_tickangle=-45, height=400)
            st.plotly_chart(fig1, use_container_width=True)
        
        with col2:
            # Pie chart
            fig2 = px.pie(segment_counts, values='Count', names='Segment',
                         title='Segment Distribution (%)',
                         hole=0.4)
            fig2.update_layout(height=400)
            st.plotly_chart(fig2, use_container_width=True)
        
        st.markdown("---")
    
    # Row 2: RFM Analysis
    if all(col in rfm.columns for col in ['Recency', 'Frequency', 'Monetary']):
        st.header("🔍 RFM Analysis")
        col1, col2 = st.columns(2)
        
        with col1:
            # RFM Heatmap
            if 'Customer_Segment' in rfm.columns:
                segment_rfm = rfm.groupby('Customer_Segment')[['Recency', 'Frequency', 'Monetary']].mean().round(2)
                
                fig3 = go.Figure(data=go.Heatmap(
                    z=segment_rfm.values.T,
                    x=segment_rfm.index,
                    y=['Recency', 'Frequency', 'Monetary'],
                    colorscale='RdYlGn_r',
                    text=segment_rfm.values.T,
                    texttemplate='%{text:.1f}',
                    textfont={"size": 10}
                ))
                fig3.update_layout(
                    title='Average RFM Values by Segment',
                    xaxis_title='Customer Segment',
                    yaxis_title='RFM Metrics',
                    height=400
                )
                st.plotly_chart(fig3, use_container_width=True)
        
        with col2:
            # 3D Scatter plot
            if 'Customer_Segment' in rfm_filtered.columns:
                fig4 = px.scatter_3d(rfm_filtered, x='Recency', y='Frequency', z='Monetary',
                                    color='Customer_Segment',
                                    title='3D RFM Visualization',
                                    labels={'Recency': 'Recency (Days)', 
                                           'Frequency': 'Frequency (Orders)',
                                           'Monetary': 'Monetary ($)'},
                                    opacity=0.7)
            else:
                fig4 = px.scatter_3d(rfm_filtered, x='Recency', y='Frequency', z='Monetary',
                                    title='3D RFM Visualization',
                                    labels={'Recency': 'Recency (Days)', 
                                           'Frequency': 'Frequency (Orders)',
                                           'Monetary': 'Monetary ($)'},
                                    opacity=0.7)
            fig4.update_layout(height=400)
            st.plotly_chart(fig4, use_container_width=True)
        
        st.markdown("---")
    
    # Row 3: Revenue Analysis
    if 'Monetary' in rfm.columns:
        st.header("💰 Revenue Analysis")
        col1, col2 = st.columns(2)
        
        with col1:
            # Revenue by segment
            if 'Customer_Segment' in rfm.columns:
                segment_revenue = rfm.groupby('Customer_Segment')['Monetary'].sum().sort_values(ascending=False).reset_index()
                segment_revenue.columns = ['Segment', 'Revenue']
                
                fig5 = px.bar(segment_revenue, x='Segment', y='Revenue',
                             title='Total Revenue by Segment',
                             color='Revenue',
                             color_continuous_scale='Blues')
                fig5.update_layout(xaxis_tickangle=-45, height=400)
                st.plotly_chart(fig5, use_container_width=True)
        
        with col2:
            # Top customers
            top_customers = rfm.nlargest(10, 'Monetary')[['Monetary']].reset_index(drop=True)
            top_customers['Customer'] = ['Customer ' + str(i+1) for i in range(len(top_customers))]
            
            fig6 = px.bar(top_customers, x='Monetary', y='Customer',
                         orientation='h',
                         title='Top 10 Customers by Revenue',
                         color='Monetary',
                         color_continuous_scale='Oranges')
            fig6.update_layout(height=400, yaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig6, use_container_width=True)
        
        st.markdown("---")
    
    # Row 4: Distributions
    if all(col in rfm_filtered.columns for col in ['Recency', 'Frequency', 'Monetary']):
        st.header("📊 RFM Distributions")
        tab1, tab2, tab3 = st.tabs(["Recency", "Frequency", "Monetary"])
        
        with tab1:
            fig7 = px.histogram(rfm_filtered, x='Recency', nbins=50,
                               title='Recency Distribution',
                               labels={'Recency': 'Days Since Last Purchase'})
            fig7.update_layout(height=350)
            st.plotly_chart(fig7, use_container_width=True)
        
        with tab2:
            fig8 = px.histogram(rfm_filtered, x='Frequency', nbins=50,
                               title='Frequency Distribution',
                               labels={'Frequency': 'Number of Purchases'})
            fig8.update_layout(height=350)
            st.plotly_chart(fig8, use_container_width=True)
        
        with tab3:
            fig9 = px.histogram(rfm_filtered, x='Monetary', nbins=50,
                               title='Monetary Distribution',
                               labels={'Monetary': 'Total Spend ($)'})
            fig9.update_layout(height=350)
            st.plotly_chart(fig9, use_container_width=True)
        
        st.markdown("---")
    
    # Segment Details Table
    if 'Customer_Segment' in rfm.columns and all(col in rfm.columns for col in ['Recency', 'Frequency', 'Monetary']):
        st.header("📋 Segment Summary Table")
        segment_summary = rfm.groupby('Customer_Segment').agg({
            'Recency': 'mean',
            'Frequency': 'mean',
            'Monetary': ['mean', 'sum', 'count']
        }).round(2)
        
        segment_summary.columns = ['Avg Recency', 'Avg Frequency', 'Avg Monetary', 'Total Revenue', 'Customer Count']
        segment_summary = segment_summary.sort_values('Total Revenue', ascending=False)
        
        st.dataframe(segment_summary, use_container_width=True)
        
        st.markdown("---")
    
    # Display raw data sample
    st.header("📄 Raw Data Sample")
    st.dataframe(rfm_filtered.head(20), use_container_width=True)
    
    # Footer
    st.markdown("---")
    st.markdown("**Created by:** Your Name | **Data Source:** UCI Online Retail Dataset")
    st.markdown("**Tech Stack:** Python, Pandas, Scikit-learn, Plotly, Streamlit")

else:
    st.error("❌ Could not load data files. Please check that 'rfm_analysis.csv' and 'cleaned_online_retail.csv' exist in the 'data' folder.")