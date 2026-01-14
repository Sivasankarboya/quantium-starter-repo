import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# Load processed data
df = pd.read_csv("data/processed_sales_data.csv")

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Sort by date
df = df.sort_values("date")

# Create line chart
fig = px.line(
    df,
    x="date",
    y="sales",
    title="Pink Morsels Sales Over Time",
    labels={
        "date": "Date",
        "sales": "Total Sales"
    }
)

# Add vertical line for price increase
fig.add_vline(
    x="2021-01-15",
    line_dash="dash",
    line_color="red"
)

# Create Dash app
app = Dash(__name__)

app.layout = html.Div([
    html.H1(
        "Impact of Pink Morsels Price Increase on Sales",
        style={"textAlign": "center"}
    ),
    dcc.Graph(figure=fig)
])

# Run server
if __name__ == "__main__":
    app.run(debug=True)

