# Reads the data, organises it and outputs it
from dash import Dash, html, dcc, callback, Input, Output
import process_data
import plotly.express as px
import pandas as pd

app = Dash()
data = process_data.do_it()
data_frame = pd.DataFrame({
    "Date": [row[1] for row in data],
    "Sales": [row[0] for row in data],
    "Region": [row[2] for row in data]
})

figure = px.line(data_frame, "Date", "Sales", "Region")

app.layout = html.Div(children=[
    html.H1(children="Pink Morsel Sales"),

    dcc.Graph(id="graph", figure=figure),

    dcc.RadioItems(
        id="radio_filter",
        options={
            "all": "All",
            "north": "North",
            "east": "East",
            "south": "South",
            "west": "West"
        },
        value="all"
    ),
])

@callback(
    Output("graph", "figure"),
    Input("radio_filter", "value")
)
def update_graph(selected_region):
    if selected_region == "all":
        filtered_df = data_frame
    else:
        filtered_df = data_frame[data_frame["Region"] == selected_region]

    return px.line(filtered_df, "Date", "Sales", "Region")


app.run(debug=True)








