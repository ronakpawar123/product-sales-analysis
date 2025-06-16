import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def top_selling_products(df):
    return df.groupby(['Month', 'Product'])['Quantity'].sum().reset_index().sort_values(['Month', 'Quantity'], ascending=[True, False])

def suggest_stock(df):
    stock_suggestion = df.groupby(['Product', 'Month'])['Quantity'].sum().reset_index()
    stock_suggestion['SuggestedQty'] = stock_suggestion.groupby('Product')['Quantity'].transform(lambda x: x.rolling(3, min_periods=1).mean().shift(1))
    return stock_suggestion.dropna()

def check_expiry(df):
    return df[df['Expiry'] == 'Yes']
