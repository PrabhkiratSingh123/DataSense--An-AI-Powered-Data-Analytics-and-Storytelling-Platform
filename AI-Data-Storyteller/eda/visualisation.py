import plotly.express as px
import pandas as pd

def plot_histogram(df: pd.DataFrame):
    numeric_cols = df.select_dtypes(include='number').columns
    if len(numeric_cols) > 0:
        return px.histogram(df, x=numeric_cols[0], title=f"Histogram of {numeric_cols[0]}")
    return "No numeric columns available for histogram."

def plot_bar(df: pd.DataFrame):
    cat_cols = df.select_dtypes(include=['object', 'category']).columns
    num_cols = df.select_dtypes(include='number').columns
    if len(cat_cols) > 0 and len(num_cols) > 0:
        summary_df = df.groupby(cat_cols[0])[num_cols[0]].sum().reset_index().head(20)
        return px.bar(summary_df, x=cat_cols[0], y=num_cols[0], title=f"Bar Chart: {cat_cols[0]} vs {num_cols[0]}")
    return "Not enough columns for bar chart (need 1 categorical, 1 numeric)."

def plot_pie(df: pd.DataFrame):
        cat_cols = df.select_dtypes(include=['object', 'category']).columns
        if len(cat_cols) > 0:
            counts = df[cat_cols[0]].value_counts().reset_index().head(10)
            counts.columns = [cat_cols[0], 'count']
            return px.pie(counts, names=cat_cols[0], values='count', title=f"Pie Chart of {cat_cols[0]}")
        return "No categorical columns available for pie chart."

def plot_scatter(df: pd.DataFrame):
    num_cols = df.select_dtypes(include='number').columns
    if len(num_cols) > 1:
        return px.scatter(df, x=num_cols[0], y=num_cols[1], title=f"Scatter Plot: {num_cols[0]} vs {num_cols[1]}")
    return "Not enough numeric columns for scatter plot (need at least 2)."

def plot_line(df: pd.DataFrame):
    num_cols = df.select_dtypes(include='number').columns
    if len(num_cols) > 1:
        sorted_df = df.sort_values(by=num_cols[0]).head(100)
        return px.line(sorted_df, x=num_cols[0], y=num_cols[1], title=f"Line Chart: {num_cols[0]} vs {num_cols[1]}")
    return "Not enough numeric columns for line chart (need at least 2)."