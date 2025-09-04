# app.py
from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px

# Load your sales data
# Replace 'sales_data.csv' with your actual file
df = pd.read_csv('formatted_sales.csv')

# Make sure the date column is datetime type
df['date'] = pd.to_datetime(df['date'])

# Sort by date
df = df.sort_values('date')

# Create a line chart
fig = px.line(
    df,
    x='date',
    y='sales',
    title='Soul Foods Sales Over Time',
    labels={'date': 'Date', 'sales': 'Sales'}
)

# Create the Dash app
app = Dash(__name__)

# Layout
app.layout = html.Div([
    html.H1("Soul Foods Sales Visualiser"),
    dcc.Graph(figure=fig)
])

# Run server
if __name__ == '__main__':
    app.run(debug=True)