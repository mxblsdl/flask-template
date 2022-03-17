from dash import Dash, dcc, html
import dash_bootstrap_components as dbc

# The flask server is passed
def init_dash(server):
    dash_app = Dash(
        server=server,
        # These parameters are passed to the layout template
        title="A Dash App",
        # The route is set in this variable instead of the routes.py file
        routes_pathname_prefix="/dashapp/",
        external_stylesheets=[
            # Adding a bootstrap 5 dependency
            # Additional css can be added here as list items
            "https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css"
        ],
    )

    dash_app.layout = html.Div(
        className="container",
        id="dash-container",
        children=[
            html.H1("Sample Dash Components"),
            dbc.Col(
                html.Div(
                    [
                        dcc.Dropdown(options=["A", "B", "C"], value="A", multi=True),
                        html.Br(),
                        dcc.RadioItems(
                            ["Apple", "Pear", "Banana", "Peach"],
                            "Pear",
                            labelStyle={"display": "block"},
                        ),
                        html.Br(),
                        dcc.Slider(1, 10, step=1),
                    ]
                ),
                width=6,
            ),
        ],
    )
    return dash_app.server
