import streamlit as st
import pandas as pd
import plotly.express as px
data=pd.read_csv("cleaned_online_retail_dataset.csv")
data["CustomerID"]=data["CustomerID"].astype(str)
st.set_page_config(page_title="Online_Ecommmerce Analysis",page_icon="📊", layout="wide")
st.markdown("""
<style>

/* ===== Global ===== */
.stApp {
    background-color: #f1f5f9;
    font-family: 'Inter', 'Segoe UI', sans-serif;
}

.block-container {
    padding: 2.5rem 3rem;
}

/* ===== HERO HEADER ===== */
.hero {
    background: linear-gradient(135deg, #2563eb, #1e40af);
    padding: 40px;
    border-radius: 22px;
    color: white;
    margin-bottom: 30px;
}
.hero h1 {
    font-size: 42px;
    margin-bottom: 5px;
}
.hero p {
    font-size: 18px;
    opacity: 0.9;
}

/* ===== KPI CARDS ===== */
.kpi-card {
    background: white;
    border-radius: 18px;
    padding: 25px;
    box-shadow: 0 12px 30px rgba(0,0,0,0.08);
    border-left: 6px solid #2563eb;
}
.kpi-title {
    color: #64748b;
    font-size: 14px;
}
.kpi-value {
    font-size: 32px;
    font-weight: 700;
    color: #0f172a;
}

/* ===== SECTION ===== */
.section {
    background: white;
    border-radius: 22px;
    padding: 30px;
    margin-bottom: 30px;
    box-shadow: 0 12px 30px rgba(0,0,0,0.06);
}
.section h2 {
    color: #0f172a;
    margin-bottom: 20px;
}

/* ===== SIDEBAR ===== */
/* Sidebar Background */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #334155, #475569);
    padding-top: 20px;
}

/* Sidebar Text */
section[data-testid="stSidebar"] * {
    color: #e5e7eb;
}

/* Sidebar Titles */
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: #bfdbfe;
}


/* ===== Hide filter labels ===== */
section[data-testid="stSidebar"] label {
    display: none !important;
}

/* ===== Multiselect & Selectbox container ===== */
section[data-testid="stSidebar"] div[data-baseweb="select"] {
    background-color: #0f172a;
    border-radius: 12px;
    padding: 4px;
}

/* ===== Selected items (tags) ===== */
section[data-testid="stSidebar"] span[data-baseweb="tag"] {
    background-color: #1d4ed8 !important;   /* Blue */
    color: #e5e7eb !important;
    border-radius: 8px !important;
    font-size: 13px;
    font-weight: 500;
}

/* ===== Remove hover red ===== */
section[data-testid="stSidebar"] span[data-baseweb="tag"]:hover {
    background-color: #2563eb !important;
}

/* ===== Dropdown arrow ===== */
section[data-testid="stSidebar"] svg {
    fill: #93c5fd !important;
}

/* ===== Placeholder text ===== */
section[data-testid="stSidebar"] div[role="combobox"] {
    color: #cbd5f5 !important;
}

/* Sidebar Divider */
section[data-testid="stSidebar"] hr {
    border-color: #475569;
}



/* ===== TABS ===== */
button[data-baseweb="tab"] {
    font-weight: 600;
    padding: 12px 20px;
}
button[data-baseweb="tab"][aria-selected="true"] {
    background-color: #2563eb;
    color: white;
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)
# KPI card function
def kpi(title, value):
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">{title}</div>
        <div class="kpi-value">{value}</div>
    </div>
    """, unsafe_allow_html=True)




# Main Title
# =============================
st.markdown("""
<div class="hero">
    <h1>📊 Online Retail Analytics Dashboard</h1>
    <p>Sales, Customers, Revenue & Business Insights</p>
</div>
""", unsafe_allow_html=True)

# =============================
# =============================
# Sidebar Filters
# =============================
st.sidebar.title("📊 Dashboard Controls")
st.sidebar.markdown("---")
st.sidebar.markdown("###  Select Years")
selected_years = st.sidebar.multiselect(
    "",
    sorted(data["year"].unique()),
    default=sorted(data["year"].unique())
)
st.sidebar.markdown("---")
st.sidebar.markdown("###  Select Countries")
selected_countries = st.sidebar.multiselect(
    "",
    sorted(data["Country"].unique()),
    default=sorted(data["Country"].unique())
)
st.sidebar.markdown("---")
st.sidebar.markdown("### Select Categories")
selected_categories = st.sidebar.multiselect(
    "",
    sorted(data["Category"].unique()),
    default=sorted(data["Category"].unique())
)

filtered_data = data[
    (data["year"].isin(selected_years)) &
    (data["Country"].isin(selected_countries)) &
    (data["Category"].isin(selected_categories))
]

# =============================
#################################Tabs######################################
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📄 Raw Data",
    "📊 Overview",
    "📦 Products & Categories",
    "🌍 Geography ",
    "👥 Customers & Payments",
    "↩️ Returns",
])
##############################Tab1######################################
with tab1:
    st.markdown("## 📄 Key Metrics about Filtered Data")
    col1, col2 = st.columns(2)
    with col1:
        number_of_rows = filtered_data.shape[0]
        kpi("Number of Rows", number_of_rows)
        kpi("Number of Invoices", f"{filtered_data['InvoiceNo'].nunique():,}")

    with col2:
        number_of_columns = filtered_data.shape[1]
        kpi("Number of Columns", number_of_columns)
        number_of_unique_customers = filtered_data["CustomerID"].nunique()
        kpi("Number of Unique Customers", number_of_unique_customers)
    st.header("📄 Filtered Data")
    st.dataframe(filtered_data.head(100), use_container_width=True)
##############################Tab2######################################
with tab2:
    st.markdown("## 📊 Overview of Online Retail Sales Data")
    st.markdown("### Key Performance Indicators")
    col1, col2 = st.columns(2)
    with col1:
        total_revenue = filtered_data["Revenue"].sum()
        kpi("Total Revenue", f"${total_revenue:,.2f}")
        total_sales = filtered_data["TotalSales"].sum()
        kpi("Total Sales", f"${total_sales:,.2f}")
    with col2:
        total_cost = filtered_data["TotalCost"].sum()
        kpi("Total Cost", f"${total_cost:,.2f}")
        Avg_order_value = filtered_data["Revenue"].mean()
        kpi("Average Order Value", f"${Avg_order_value:,.2f}")
    
    col3,col4=st.columns(2)
    with col3:
        st.markdown("### Monthly Analysis of Total Cost")
        # monthly analysis of total cost
        monthly_anlysis = filtered_data.groupby('month')['TotalCost'].sum().reset_index()
        fig1=px.line(monthly_anlysis, x='month', y='TotalCost',markers=True, labels={'month':'Month', 'TotalCost':'Total Cost'})
        st.plotly_chart(fig1, use_container_width=True)
        # daily analysis of total cost
        Daily_anlysis = filtered_data.groupby('day')['TotalCost'].sum().sort_values(ascending=False).reset_index()
        fig2=px.bar(Daily_anlysis, x='day', y='TotalCost', labels={'day':'Day', 'TotalCost':'Total Cost'})
        st.markdown("### Daily Analysis of Total Cost")
        st.plotly_chart(fig2, use_container_width=True)
        # distribution of unit prices

        fig3 = px.histogram(
            filtered_data,
            x='UnitPrice',
            nbins=50,
            color_discrete_sequence=['#2E86AB']
        )
        fig3.update_layout(showlegend=False)
        st.markdown("### Distribution of Unit Prices")
        st.plotly_chart(fig3, use_container_width=True)
    with col4:
        # yearly analysis of total cost
        yearly_analysis = filtered_data.groupby('year')['TotalCost'].sum().reset_index()
        fig4=px.line(yearly_analysis, x='year', y='TotalCost', labels={'year':'Year', 'TotalCost':'Total Cost'})
        st.markdown("### Yearly Analysis of Total Cost")
        st.plotly_chart(fig4, use_container_width=True)
        #check the relation between Discount and Revenue
        discount_revenue = filtered_data.groupby('Discount')['TotalSales'].sum().reset_index()
        fig5=px.scatter(discount_revenue, x='Discount', y='TotalSales', labels={'Discount':'Discount', 'TotalSales':'Total Sales'})
        st.markdown("### Discount vs Total Sales")
        st.plotly_chart(fig5, use_container_width=True)
        # scatter plot of UnitPrice vs Quantity colored by Category
        sample_df = filtered_data.sample(min(1000, len(filtered_data)))
        fig6 = px.scatter(
            sample_df,
            x='UnitPrice',
            y='Quantity',
            color='Category',
            size='Revenue',
            #opacity=0.6
        )
        st.markdown("### Unit Price vs Quantity by Category")
        st.plotly_chart(fig6, use_container_width=True)

##############################Tab3######################################
with tab3:
    st.markdown("## 📦 Products & Categories Analysis")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Top 10 Products by Revenue")
        # Top 10 products with hieghest revenues
        top10_products = filtered_data.groupby("Description")["Revenue"].sum()  
        top10_products= top10_products.sort_values(ascending=False).reset_index().head(10)
        fig1=px.bar(top10_products, x='Description', y='Revenue', labels={'Description':'Product Description', 'Revenue':'Revenue'})
        st.plotly_chart(fig1, use_container_width=True)
    with col2:
        st.markdown("### Revenue by Category")
        #analysis category by revenue
        category_revenue = filtered_data.groupby('Category')['Revenue'].sum().sort_values(ascending=False).reset_index()
        fig2 = px.pie(category_revenue, values="Revenue", names="Category", hole=0.4)
        fig2.update_traces(textinfo="percent+label")
        fig2.update_layout(template="plotly_white")
        st.plotly_chart(fig2, use_container_width=True)
##############################Tab4######################################
with tab4:
    st.markdown("## 🌍 Geography Analysis")
    col1, col2 = st.columns(2)
    with col1:
        # top countries by total sales 
        country_TotalSale =filtered_data.groupby('Country')['TotalSales'].sum().sort_values(ascending=False).reset_index()
        fig1=px.pie(country_TotalSale.head(10), names='Country', values='TotalSales')
        fig1.update_traces(textinfo="percent+label")
        fig1.update_layout(template="plotly_white")
        st.markdown("### Top 10 Countries by Total Sales")
        st.plotly_chart(fig1, use_container_width=True)
        # sales by warehouse location
        warehouse_sales = filtered_data.groupby('WarehouseLocation')['Revenue'].sum().reset_index().sort_values(by="Revenue", ascending=False)
        fig2=px.bar(warehouse_sales, x='WarehouseLocation', y='Revenue', labels={'WarehouseLocation':'Warehouse Location', 'Revenue':'Revenue'})
        st.markdown("### Sales by Warehouse Location")
        st.plotly_chart(fig2, use_container_width=True)
    with col2:
        # top countries by revenue
        country_revenue = filtered_data.groupby('Country')['Revenue'].sum().sort_values(ascending=False).reset_index()
        fig3=px.pie(country_revenue.head(10), names='Country', values='Revenue')
        fig3.update_traces(textinfo="percent+label")
        fig3.update_layout(template="plotly_white")
        st.markdown("### Top 10 Countries by Revenue")
        st.plotly_chart(fig3, use_container_width=True)
        # shipment provider performance by revenue
        ShipmentProvider_performance = filtered_data.groupby('ShipmentProvider')["Revenue"].sum().sort_values(ascending=False).reset_index()
        fig4=px.bar(ShipmentProvider_performance, x='ShipmentProvider', y='Revenue', labels={'ShipmentProvider':'Shipment Provider', 'Revenue':'Revenue'})
        st.markdown("### Shipment Provider Performance by Revenue")
        st.plotly_chart(fig4, use_container_width=True)

##############################Tab5######################################
with tab5:
    st.markdown("## 👥 Customers & Payments Analysis")
    col1, col2 = st.columns(2)
    with col1:
        # analyze payment methods used by customers
        payment_method_counts = filtered_data['PaymentMethod'].value_counts().reset_index()
        payment_method_counts.columns = ['PaymentMethod', 'Count']
        fig1=px.pie(payment_method_counts, names='PaymentMethod', values='Count')
        fig1.update_traces(textinfo="percent+label")
        fig1.update_layout(template="plotly_white")
        st.markdown("### Payment Methods Used by Customers")
        st.plotly_chart(fig1, use_container_width=True)
        # sales by sales channel
        sales_by_channel = filtered_data.groupby('SalesChannel')['TotalSales'].sum().reset_index()
        fig2=px.bar(sales_by_channel, x='SalesChannel', y='TotalSales', labels={'SalesChannel':'Sales Channel', 'TotalSales':'Total Sales'})
        st.markdown("### Sales by Sales Channel")
        st.plotly_chart(fig2, use_container_width=True)
    with col2:
        st.markdown("### Top 10 Customers by Total Cost")
        # Top 10 customers by total Total cost 
        top10_customers = filtered_data.groupby("CustomerID")["TotalCost"].sum() 
        top10_customers= top10_customers.sort_values(ascending=False).head(10)
        fig3=px.bar(top10_customers.reset_index(), x='CustomerID', y='TotalCost', labels={'CustomerID':'Customer ID', 'TotalCost':'Total Cost'})
        fig3.update_layout(
        xaxis_type="category"    
        )
        st.plotly_chart(fig3, use_container_width=True)
        # unique customers per year
        customers_per_year = (filtered_data.groupby("year")["CustomerID"].nunique().reset_index(name="Number_of_Customers"))
        fig4=px.bar(customers_per_year, x='year', y='Number_of_Customers', labels={'year':'Year', 'Number_of_Customers':'Number of Customers'})
        fig4.update_layout(
            xaxis_type="category"       
        )
        st.markdown("### Number of Unique Customers per Year")
        st.plotly_chart(fig4, use_container_width=True)

##############################Tab6######################################
with tab6:
    returns = filtered_data["ReturnStatus"].value_counts().reset_index()
    returns.columns = ["ReturnStatus", "Count"]
    c1, c2, c3 = st.columns(3)

    fig1 = px.bar(returns, x="ReturnStatus", y="Count")
    fig1.update_layout(template="plotly_white")
    c1.plotly_chart(fig1, use_container_width=True)
    with c2:
        kpi("Return Rate", f"{(filtered_data['ReturnStatus']=='Returned').mean()*100:.1f}%")
    with c3:
        kpi("Total Returns", f"{(filtered_data['ReturnStatus']=='Returned').sum():,}")
    col1,col2=  st.columns(2)
    with col1:
        # top returned products
        top_returned_products = (filtered_data[filtered_data['ReturnStatus'] == 'Returned'].groupby('Description').size().reset_index(name='ReturnCount').sort_values(by='ReturnCount', ascending=False).head(10)
        )
        fig2=px.bar(top_returned_products, x='Description', y='ReturnCount', labels={'Description':'Product Description', 'ReturnCount':'Return Count'})
        st.markdown("### Top 10 Returned Products by Return Count")
        st.plotly_chart(fig2, use_container_width=True)
    with col2:
        returns_per_year = filtered_data[filtered_data["ReturnStatus"] == "Returned"].groupby("year").size().reset_index(name="Returned_Count")
        fig3 = px.bar(returns_per_year,x="year",y="Returned_Count",labels={"year": "Year", "Returned_Count": "Number of Returns"})
        fig3.update_layout(
            template="plotly_white",
            xaxis_type="category"
        )
        st.markdown("### Number of Returned Items per Year")
        st.plotly_chart(fig3, use_container_width=True)
