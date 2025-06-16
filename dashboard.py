import streamlit as st
import pandas as pd
import main

st.title("📊 Product Sales Analysis Dashboard")

df = main.load_data('sales_data.csv')

st.subheader("1. Monthly Top Selling Products")
top_products = main.top_selling_products(df)
st.dataframe(top_products)

st.subheader("2. Suggested Stock for Next Month")
stock_df = main.suggest_stock(df)
st.dataframe(stock_df)

st.subheader("3. Products Near Expiry")
expiry_df = main.check_expiry(df)
st.dataframe(expiry_df)
