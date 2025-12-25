# Online Retail Data Analysis Project

## Project Overview

This project analyzes a real-world Online Retail dataset to extract
business insights related to sales performance, customer behavior, and
revenue trends using Python.

The dataset is intentionally not clean and includes missing values,
duplicated records, invalid transactions to simulate
real-world data challenges.

------------------------------------------------------------------------

## Business Questions

-   What are the top-selling products?
-   Which countries generate the highest revenue?
-   Is there seasonality in sales?
-   Who are the most valuable customers?
-   What factors affect total revenue?
-   what average Discount by Year
-   what is the most shippment provider performance 
-   what is the most sale channels used
------------------------------------------------------------------------

## Dataset Description

-   Each row represents a retail transaction.
-   Columns include InvoiceNo', 'StockCode', 'Description', 'Quantity', 'InvoiceDate',
       'UnitPrice', 'CustomerID', 'Country', 'Discount', 'PaymentMethod',
       'ShippingCost', 'Category', 'SalesChannel', 'ReturnStatus',
       'ShipmentProvider', 'WarehouseLocation', 'OrderPriority'
-   Data issues include missing values, duplicates, negative quantities
    (returns) and incorrect data

------------------------------------------------------------------------

## Data Cleaning Steps

-   Removed duplicated records.
-   Dropped rows with missing CustomerID.
-   Removed invalid transactions (Quantity \<= 0 or UnitPrice \<= 0).
-   Converted InvoiceDate to datetime format.
-   Created new features:
    -   TotalSales = Quantity \* UnitPrice
    -   TotalCost= TotalSales \* (1-Discount) + ShippingCost
    -   Revenue=  TotalSales \* (1-Discount)
    -   Month, Day, Hour extracted from InvoiceDate

------------------------------------------------------------------------

## Exploratory Data Analysis (EDA)

-   Univariate analysis on Quantity and UnitPrice.
-   Bivariate and multivariate analysis on revenue by country, month,
    and customer.
-   Customer behavior and product performance analysis.

### Visualization Types Used

-   Bar charts
-   Histograms
-   Line charts
-   pie charts
-   Scatter plots

------------------------------------------------------------------------

## How to Run the Project

### Prerequisites

-   pandas==2.3.3
-   plotly==6.5.0
-   streamlit==1.52.2
-   Jupyter Notebook or Jupyter Lab

### Clone the Repository

``` bash
git clone https://github.com/ahmedkh20122000-blip/Online_retail_dataset_analysis.git
cd Online_retail_dataset_analysis
```

Or download the repository as a ZIP file and extract it.

### Install Required Libraries

``` bash
pip install pandas numpy plotly 
```

### Run the Notebook

``` bash
jupyter notebook
```

Open the notebook file:

    Online_Retail_Analysis.ipynb

Run all cells sequentially from top to bottom.

------------------------------------------------------------------------

## Repository Structure

       ├── online_retail_snalysis.ipynb  #Notebook Analysis
       ├── online_retail_analysis.py   # Streamlit Dashboard
       ├── README.md                   # Project Description
       ├── online_retail_dataset.csv   # Original Data
       ├── cleaned_online_retail_dataset.csv   #Data After cleaning
       ├── requirements.Txt            # Needed library

------------------------------------------------------------------------

## Tools & Technologies

-   Python
-   Pandas
-   NumPy
-   plotly
-   Jupyter Notebook

------------------------------------------------------------------------

## Author

**Ahmed Khaled**  
Data Analyst 
📍 Egypt

## 🎥 Demo Video

🔗 https://drive.google.com/file/d/1lttIPKicuAwEGClHOLZypdy3EDvHlVHp/view?usp=sharing 

## Interactive Streamlit Dashboard: 

🔗 [Open Dashboard](https://onlineretaildatasetanalysis-bg6otlobvffs4dd3fdw8hk.streamlit.app/)

------------------------------------------------------------------------

"It's your time to shine ❤️"
