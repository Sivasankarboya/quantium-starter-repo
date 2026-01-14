from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# -------------------------------
# Load data
# -------------------------------
df = pd.read_csv("data/processed_sales_data.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# -------------------------------
# Create Dash app
# -------------------------------
app = Dash(__name__)

# -------------------------------
# Layout
# -------------------------------
app.layout = html.Div([

    html.H2("Pink Morsels Sales Dashboard"),

    # Region selector (UI requirement)
    dcc.RadioItems(
        id="region-radio",
        options=[
            {"label": "All", "value": "all"},
            {"label": "North", "value": "north"},
            {"label": "East", "value": "east"},
            {"label": "South", "value": "south"},
            {"label": "West", "value": "west"},
        ],
        value="all",
        inline=True
    ),

    dcc.Graph(id="sales-line-chart")
])

# -------------------------------
# Callback (safe, no region data)
# -------------------------------
@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-radio", "value")
)
def update_sales_chart(selected_region):

    # No region data available — show overall sales
    fig = px.line(
        df,
        x="date",
        y="sales",
        title="Pink Morsels Total Sales Over Time",
        markers=True
    )

    return fig

# -------------------------------
# Run server
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)

