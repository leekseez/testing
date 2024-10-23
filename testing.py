# streamlit_dashboard.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Name of the dashboard
st.title("Sales Dashboard - Continental BGS")

# Sidebar for user inputs
st.sidebar.header("Filter Sales Data")
year = st.sidebar.selectbox("Select Year", [2022, 2023, 2024])
region = st.sidebar.multiselect("Select Region", ["North America", "Europe", "Asia", "South America", "Africa"])

# Simulated sales data for demonstration purposes
def load_sales_data():
    data = {
        'Year': [2022, 2022, 2023, 2023, 2024, 2024],
        'Region': ['North America', 'Europe', 'Asia', 'South America', 'Africa', 'Europe'],
        'Sales': [20000, 15000, 25000, 18000, 30000, 21000]
    }
    df = pd.DataFrame(data)
    return df

# Load sales data
sales_data = load_sales_data()

# Filter sales data based on the sidebar inputs
filtered_data = sales_data[(sales_data['Year'] == year) & (sales_data['Region'].isin(region))]

# Display filtered data
st.subheader(f"Sales Data for {year}")
st.write(filtered_data)

# Plot sales chart
if not filtered_data.empty:
    fig, ax = plt.subplots()
    filtered_data.plot(kind='bar', x='Region', y='Sales', ax=ax, color='skyblue')
    ax.set_ylabel("Sales in USD")
    ax.set_title(f"Sales in {year}")
    st.pyplot(fig)
else:
    st.write("No data available for the selected filters.")

# Summary statistics
st.subheader("Sales Summary")
total_sales = filtered_data['Sales'].sum()
st.write(f"Total Sales: ${total_sales:,}")
