# Reads the data, organises it and outputs it
from dash import Dash, html, dcc, Input, Output, callback
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


])

app.run(debug=True)








