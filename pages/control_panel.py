import dash
import time
import pathlib
import os
import random

import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import State, Input, Output
import dash_daq as daq


dash.register_page(__name__, path="/", name="Control Panel 🎛️")

# Initialize a global variable to store the running time
start_time = time.time() - random.randint(0, 172800)
running_seconds = 0

current_vibration = random.randint(30, 35)
current_weight = 0

# Mapbox
MAPBOX_ACCESS_TOKEN = (
    "pk.eyJ1IjoicGxvdGx5bWFwYm94IiwiYSI6ImNrOWJqb2F4djBnMjEzbG50amg0dnJieG4ifQ.Zme1-Uzoi75IaFbieBDl3A"
)
MAPBOX_STYLE = "mapbox://styles/plotlymapbox/cjyivwt3i014a1dpejm5r7dwr"

# Dash_DAQ elements


time_now = html.Div(
    id="control-panel-time-now",
    children=[
        daq.LEDDisplay(
            id="control-panel-time-now-component",
            value="00:00:00",
            label="Time Now",
            size=40,
            color="#fec036",
            backgroundColor="#2b2b2b",
        )
    ],
    n_clicks=0,
)

mnkhal = html.Div(
    id="control-panel-speed",
    children=[
        html.Img(
            id="control-panel-speed-image",
            src="./assets/mnkhal-side.png",  # Replace this with the actual path or URL to your image
            alt="Speed Gauge Image",  # Alternative text for the image
            style={"width": "320px", "height": "175px"},  # Adjust the size as needed
        )
    ],
    n_clicks=0,
)

crop = html.Div(
    id="control-panel-speed",
    children=[
        html.Img(
            id="control-panel-speed-image",
            src="./assets/mnkhal-top.png",  # Replace this with the actual path or URL to your image
            alt="Speed Gauge Image",  # Alternative text for the image
            style={"width": "220px", "height": "120px"},  # Adjust the size as needed
        )
    ],
    n_clicks=0,
)

switch_toggle = daq.BooleanSwitch(
    id='tooltips-toggle', on=True, label='Tooltips are On',
    labelPosition='top',
    style={"color": "#black"},
    color='#ffe102',
    )

running_time = html.Div(
    id="control-panel-running-time",
    children=[
        daq.LEDDisplay(
            id="control-panel-running-time-component",
            value="00:00:00",
            label="Running Time",
            size=40,
            color="#fec036",
            backgroundColor="#2b2b2b",
        )
    ],
    n_clicks=0,
)

speed = html.Div(
    id="control-panel-speed",
    children=[
        daq.Gauge(
            id="control-panel-speed-component",
            label="Speed",
            min=0,
            max=40,
            showCurrentValue=True,
            value=27.859,
            size=175,
            units="1000km/h",
            color="#fec036",
        )
    ],
    n_clicks=0,
)

weight = html.Div(
    id="control-panel-weight",
    children=[
        daq.Tank(
            id="control-panel-weight-component",
            label="Weight",
            min=0,
            max=50,
            value=14,
            units="kilomgrams",
            showCurrentValue=True,
            color="#303030",
        )
    ],
    n_clicks=0,
)

vibration = html.Div(
    id="control-panel-vibration",
    children=[
        daq.LEDDisplay(
            id="control-panel-vibration-component",
            value="000.00",
            label="Vibration",
            size=24,
            color="#fec036",
            style={"color": "#black"},
            backgroundColor="#2b2b2b",
        )
    ],
    n_clicks=0,
)

fan_speed = html.Div(
    id="control-panel-speed",
    children=[
        daq.Gauge(
            id="control-panel-fan-speed-component",
            label="Fan Speed",
            min=0,
            max=40,
            showCurrentValue=True,
            value=27.859,
            size=175,
            units="1000km/h",
            color="#fec036",
        )
    ],
    n_clicks=0,
)

capacity = html.Div(
    id="control-panel-capacity",
    children=[
        daq.GraduatedBar(
            id="control-panel-capacity-component",
            label="Capacity Level",
            min=0,
            max=100,
            value=76,
            step=1,
            showCurrentValue=True,
            color="#fec036",
        )
    ],
    n_clicks=0,
)

elevation = html.Div(
    id="control-panel-elevation",
    children=[
        daq.Tank(
            id="control-panel-elevation-component",
            label="Elevation",
            min=0,
            max=1000,
            value=650,
            units="kilometers",
            showCurrentValue=True,
            color="#303030",
        )
    ],
    n_clicks=0,
)

temperature = html.Div(
    id="control-panel-temperature",
    children=[
        daq.Tank(
            id="control-panel-temperature-component",
            label="Temperature",
            min=0,
            max=500,
            value=290,
            units="Kelvin",
            showCurrentValue=True,
            color="#303030",
        )
    ],
    n_clicks=0,
)

fuel_indicator = html.Div(
    id="control-panel-fuel",
    children=[
        daq.GraduatedBar(
            id="control-panel-fuel-component",
            label="Fuel Level",
            min=0,
            max=100,
            value=76,
            step=1,
            showCurrentValue=True,
            color="#fec036",
        )
    ],
    n_clicks=0,
)

battery_indicator = html.Div(
    id="control-panel-battery",
    children=[
        daq.GraduatedBar(
            id="control-panel-battery-component",
            label="Battery-Level",
            min=0,
            max=100,
            value=85,
            step=1,
            showCurrentValue=True,
            color="#fec036",
        )
    ],
    n_clicks=0,
)

longitude = html.Div(
    id="control-panel-longitude",
    children=[
        daq.LEDDisplay(
            id="control-panel-longitude-component",
            value="0000.0000",
            label="Longitude",
            size=24,
            color="#fec036",
            style={"color": "#black"},
            backgroundColor="#2b2b2b",
        )
    ],
    n_clicks=0,
)

latitude = html.Div(
    id="control-panel-latitude",
    children=[
        daq.LEDDisplay(
            id="control-panel-latitude-component",
            value="0050.9789",
            label="Latitude",
            size=24,
            color="#fec036",
            style={"color": "#black"},
            backgroundColor="#2b2b2b",
        )
    ],
    n_clicks=0,
)

solar_panel_0 = daq.Indicator(
    className="panel-lower-indicator",
    id="control-panel-solar-panel-0",
    label="Solar-Panel-0",
    labelPosition="bottom",
    value=True,
    color="#fec036",
    style={"color": "#black"},
)

solar_panel_1 = daq.Indicator(
    className="panel-lower-indicator",
    id="control-panel-solar-panel-1",
    label="Solar-Panel-1",
    labelPosition="bottom",
    value=True,
    color="#fec036",
    style={"color": "#black"},
)

camera = daq.Indicator(
    className="panel-lower-indicator",
    id="control-panel-camera",
    label="Camera",
    labelPosition="bottom",
    value=True,
    color="#fec036",
    style={"color": "#black"},
)

thrusters = daq.Indicator(
    className="panel-lower-indicator",
    id="control-panel-thrusters",
    label="Thrusters",
    labelPosition="bottom",
    value=True,
    color="#fec036",
    style={"color": "#black"},
)

motor = daq.Indicator(
    className="panel-lower-indicator",
    id="control-panel-motor",
    label="Motor",
    labelPosition="bottom",
    value=True,
    color="#fec036",
    style={"color": "#black"},
)

communication_signal = daq.Indicator(
    className="panel-lower-indicator",
    id="control-panel-communication-signal",
    label="Signal",
    labelPosition="bottom",
    value=False,
    color="#fec036",
    style={"color": "#red"},
)

map_toggle = daq.ToggleSwitch(
    id="control-panel-toggle-map",
    value=True,
    label=["Hide path", "Show path"],
    color="#ffe102",
    style={"color": "#black"},
)

minute_toggle = daq.ToggleSwitch(
    id="control-panel-toggle-minute",
    value=True,
    label=["Past Hour", "Past Minute"],
    color="#ffe102",
    style={"color": "#black"},
)

# Side panel

satellite_dropdown = dcc.Dropdown(
    id="satellite-dropdown-component",
    options=[
        {"label": "Mnkhal 1", "value": "Mnkhal 1"},
        {"label": "Mnkhal 2", "value": "Mnkhal 2"},
        {"label": "Mnkhal 3", "value": "Mnkhal 3"},
        {"label": "Mnkhal 4", "value": "Mnkhal 4"},
    ],
    clearable=False,
    value="Mnkhal 1",
)

satellite_dropdown_text = html.P(id="satellite-dropdown-text", children=["Mnkhal", html.Br(), "Machines"])

satellite_title = html.H1(id="satellite-name", children="")

satellite_body = html.P(className="satellite-description", id="satellite-description", children=[""])

side_panel_layout = html.Div(
    id="panel-side",
    children=[
        satellite_dropdown_text,
        html.Div(id="satellite-dropdown", children=satellite_dropdown),
        html.Div(id="panel-side-text", children=[satellite_title, satellite_body]),
    ],
)


# Helper to straighten lines on the map
def flatten_path(xy1, xy2):
    diff_rate = (xy2 - xy1) / 100
    res_list = []
    for i in range(100):
        res_list.append(xy1 + i * diff_rate)
    return res_list


map_data = [
    {
        "type": "scattermapbox",
        "lat": [0],
        "lon": [0],
        "hoverinfo": "text+lon+lat",
        "text": "Satellite Path",
        "mode": "lines",
        "line": {"width": 2, "color": "#707070"},
    },
    {
        "type": "scattermapbox",
        "lat": [0],
        "lon": [0],
        "hoverinfo": "text+lon+lat",
        "text": "Current Position",
        "mode": "markers",
        "marker": {"size": 10, "color": "#fec036"},
    },
]

map_layout = {
    "mapbox": {
        "accesstoken": MAPBOX_ACCESS_TOKEN,
        "style": MAPBOX_STYLE,
        "center": {"lat": 45},
    },
    "showlegend": False,
    "autosize": True,
    "paper_bgcolor": "#1e1e1e",
    "plot_bgcolor": "#1e1e1e",
    "margin": {"t": 0, "r": 0, "b": 0, "l": 0},
}

map_graph = html.Div(
    id="world-map-wrapper",
    children=[
        map_toggle,
        dcc.Graph(
            id="world-map",
            figure={"data": map_data, "layout": map_layout},
            config={"displayModeBar": False, "scrollZoom": False},
        ),
    ],
)

# Histogram

histogram = html.Div(
    id="histogram-container",
    children=[
        html.Div(
            id="histogram-header",
            children=[
                html.H1(id="histogram-title", children=["Select A Property To Display"]),
                minute_toggle,
            ],
        ),
        dcc.Graph(
            id="histogram-graph",
            figure={
                "data": [
                    {
                        "x": [i for i in range(60)],
                        "y": [i for i in range(60)],
                        "type": "scatter",
                        "marker": {"color": "#fec036"},
                    }
                ],
                "layout": {
                    "margin": {"t": 30, "r": 35, "b": 40, "l": 50},
                    "xaxis": {"dtick": 5, "gridcolor": "#636363", "showline": False},
                    "yaxis": {"showgrid": False},
                    "plot_bgcolor": "#2b2b2b",
                    "paper_bgcolor": "#2b2b2b",
                    "font": {"color": "gray"},
                },
            },
            config={"displayModeBar": False},
        ),
    ],
)

indecators = html.Div(
        id="panel-lower-1",
        children=[
            html.Div(
                id="panel-lower-indicators",
                children=[
                    # html.Div(
                    #     id="panel-lower-indicators-0",
                    #     children=[solar_panel_0, thrusters],
                    # ),
                    html.Div(
                        id="panel-lower-indicators-2",
                        children=[camera, communication_signal],
                    ),
                ],
            ),
            # html.Div(
            #     id="panel-lower-graduated-bars",
            #     children=[fuel_indicator, battery_indicator],
            # ),
        ],
    )


first_row = html.Div(
    [
        switch_toggle,
        running_time,
        time_now,
    ],
    style={
        'display': 'flex',
        'flexDirection': 'row',  # Arrange items in a column
        'justifyContent': 'center',  # Center vertically
        'alignItems': 'center',  # Center horizontally
        'textAlign': 'center',
        'gap': '120px',  # Add spacing between the elements,
        'marginBottom': '70px'  # Space between rows
    }
)

second_row = html.Div(
    [
        # First Column
        html.Div(
            [
                # First Row inside First Column
                html.Div(
                    [
                        vibration, 
                        indecators,                         fan_speed, 

                    ],
                    style={
                        'display': 'flex',
                        'flexDirection': 'row',  # Arrange items in a row
                        'justifyContent': 'center',
                        'alignItems': 'center',  # Center horizontally
                        'gap': '40px',  # Add spacing between vibration and indecators
                    }
                ),
                # Second Row inside First Column
                html.Div(
                    [
                        capacity
                    ],
                    style={
                        'display': 'flex',
                        'flexDirection': 'row',  # Arrange items in a row
                        'justifyContent': 'center',
                        'alignItems': 'center',  # Center horizontally
                        'gap': '40px',  # Add spacing between fan_speed and capacity
                    }
                )
            ],
            style={
                'display': 'flex',
                'flexDirection': 'column',  # Arrange rows in a column
                'alignItems': 'center',
                'textAlign': 'center',
                'gap': '20px',  # Add spacing between the two rows
            }
        ),

        # Second Column
        html.Div(
            [
                mnkhal
            ],
            style={
                'display': 'flex',
                'flexDirection': 'column',  # Arrange items in a column
                'alignItems': 'center',
                'textAlign': 'center',
            }
        ),

        # Third Column
        html.Div(
            [
                weight,
                crop,
            ],
            style={
                'display': 'flex',
                'flexDirection': 'row',  # Arrange items in a column
                'alignItems': 'center',
                'textAlign': 'center',
            }
        ),
    ],
    style={
        'display': 'flex',
        'flexDirection': 'row',  # Arrange items in a column
        'justifyContent': 'center',  # Center vertically
        'alignItems': 'center',  # Center horizontally
        'textAlign': 'center',
        'gap': '3px'  # Add spacing between the elements
    }
)


# Control panel + map
main_panel_layout = html.Div(
    id="panel-upper-lower",
    children=[
        dcc.Interval(id="interval", interval=1 * 2000, n_intervals=0),
        # map_graph,
        first_row,
        second_row,
        # html.Div(
        #     id="panel",
        #     children=[
        #         # histogram,
        #         html.Div(
        #             id="panel-lower",
        #             children=[
        #                 html.Div(
        #                     id="panel-lower-0",
        #                     children=[elevation, temperature, speed],
        #                 ),
        #                 mnkhal,
        #                 html.Div(
        #                     id="panel-lower-1",
        #                     children=[
        #                         html.Div(
        #                             id="panel-lower-led-displays",
        #                             children=[latitude, longitude],
        #                         ),
        #                         html.Div(
        #                             id="panel-lower-indicators",
        #                             children=[
        #                                 html.Div(
        #                                     id="panel-lower-indicators-0",
        #                                     children=[solar_panel_0, thrusters],
        #                                 ),
        #                                 html.Div(
        #                                     id="panel-lower-indicators-1",
        #                                     children=[solar_panel_1, motor],
        #                                 ),
        #                                 html.Div(
        #                                     id="panel-lower-indicators-2",
        #                                     children=[camera, communication_signal],
        #                                 ),
        #                             ],
        #                         ),
        #                         html.Div(
        #                             id="panel-lower-graduated-bars",
        #                             children=[fuel_indicator, battery_indicator],
        #                         ),
        #                     ],
        #                 ),
        #             ],
        #             style={
        #                 "display": "flex",
        #                 "justify-content": "center",
        #                 "align-items": "center",
        #                 "height": "100%",  # Ensure the Div takes up the available space if needed
        #                 "text-align": "center",
        #             },
        #         ),
        #     ],
        # ),
    ],
    style={
        'display': 'flex',
        'flexDirection': 'column',  # Arrange rows in a column
        'justifyContent': 'center',  # Center vertically within the container
        'alignItems': 'center',  # Center horizontally within the container
        'height': '100vh',  # Full height of the viewport
        'textAlign': 'center'
    }
)

# Data generation

# Pandas
APP_PATH = str(pathlib.Path(__file__).parent.resolve())

# Satellite H45-K1 data
df_non_gps_h_0 = pd.read_csv(os.path.join(APP_PATH, os.path.join("../data", "non_gps_data_h_0.csv")))
df_non_gps_m_0 = pd.read_csv(os.path.join(APP_PATH, os.path.join("../data", "non_gps_data_m_0.csv")))
df_gps_m_0 = pd.read_csv(os.path.join(APP_PATH, os.path.join("../data", "gps_data_m_0.csv")))
df_gps_h_0 = pd.read_csv(os.path.join(APP_PATH, os.path.join("../data", "gps_data_h_0.csv")))

# Satellite L12-5 data
df_non_gps_h_1 = pd.read_csv(os.path.join(APP_PATH, os.path.join("../data", "non_gps_data_h_1.csv")))
df_non_gps_m_1 = pd.read_csv(os.path.join(APP_PATH, os.path.join("../data", "non_gps_data_m_1.csv")))
df_gps_m_1 = pd.read_csv(os.path.join(APP_PATH, os.path.join("../data", "gps_data_m_1.csv")))
df_gps_h_1 = pd.read_csv(os.path.join(APP_PATH, os.path.join("../data", "gps_data_h_1.csv")))

# Root
root_layout = html.Div(
    id="root",
    children=[
        dcc.Store(id="store-placeholder"),
        dcc.Store(
            id="store-data",
            data={
                "hour_data_0": {
                    "elevation": [df_non_gps_h_0["elevation"][i] for i in range(60)],
                    "temperature": [df_non_gps_h_0["temperature"][i] for i in range(60)],
                    "speed": [df_non_gps_h_0["speed"][i] for i in range(60)],
                    "latitude": ["{0:09.4f}".format(df_gps_h_0["lat"][i]) for i in range(60)],
                    "longitude": ["{0:09.4f}".format(df_gps_h_0["lon"][i]) for i in range(60)],
                    "fuel": [df_non_gps_h_0["fuel"][i] for i in range(60)],
                    "battery": [df_non_gps_h_0["battery"][i] for i in range(60)],
                },
                "minute_data_0": {
                    "elevation": [df_non_gps_m_0["elevation"][i] for i in range(60)],
                    "temperature": [df_non_gps_m_0["temperature"][i] for i in range(60)],
                    "speed": [df_non_gps_m_0["speed"][i] for i in range(60)],
                    "latitude": ["{0:09.4f}".format(df_gps_m_0["lat"][i]) for i in range(60)],
                    "longitude": ["{0:09.4f}".format(df_gps_m_0["lon"][i]) for i in range(60)],
                    "fuel": [df_non_gps_m_0["fuel"][i] for i in range(60)],
                    "battery": [df_non_gps_m_0["battery"][i] for i in range(60)],
                },
                "hour_data_1": {
                    "elevation": [df_non_gps_h_1["elevation"][i] for i in range(60)],
                    "temperature": [df_non_gps_h_1["temperature"][i] for i in range(60)],
                    "speed": [df_non_gps_h_1["speed"][i] for i in range(60)],
                    "latitude": ["{0:09.4f}".format(df_gps_h_1["lat"][i]) for i in range(60)],
                    "longitude": ["{0:09.4f}".format(df_gps_h_1["lon"][i]) for i in range(60)],
                    "fuel": [df_non_gps_h_1["fuel"][i] for i in range(60)],
                    "battery": [df_non_gps_h_1["battery"][i] for i in range(60)],
                },
                "minute_data_1": {
                    "elevation": [df_non_gps_m_1["elevation"][i] for i in range(60)],
                    "temperature": [df_non_gps_m_1["temperature"][i] for i in range(60)],
                    "speed": [df_non_gps_m_1["speed"][i] for i in range(60)],
                    "latitude": ["{0:09.4f}".format(df_gps_m_1["lat"][i]) for i in range(60)],
                    "longitude": ["{0:09.4f}".format(df_gps_m_1["lon"][i]) for i in range(60)],
                    "fuel": [df_non_gps_m_1["fuel"][i] for i in range(60)],
                    "battery": [df_non_gps_m_1["battery"][i] for i in range(60)],
                },
            },
        ),
        # For the case no components were clicked, we need to know what type of graph to preserve
        dcc.Store(id="store-data-config", data={"info_type": "", "satellite_type": 0}),
        side_panel_layout,
        main_panel_layout,
    ],
)


# Callbacks Data


# Add new data every second/minute
@dash.callback(
    Output("store-data", "data"),
    [Input("interval", "n_intervals")],
    [State("store-data", "data")],
)
def update_data(interval, data):
    new_data = data
    # Update H45-K1 data when sat==0, update L12-5 data when sat==1
    for sat in range(2):
        if sat == 0:
            gps_minute_file = df_gps_m_0
            gps_hour_file = df_gps_h_0
        else:
            gps_minute_file = df_gps_m_1
            gps_hour_file = df_gps_h_1

        m_data_key = "minute_data_" + str(sat)
        h_data_key = "hour_data_" + str(sat)

        new_data[m_data_key]["elevation"].append(data[m_data_key]["elevation"][0])
        new_data[m_data_key]["elevation"] = new_data[m_data_key]["elevation"][1:61]
        new_data[m_data_key]["temperature"].append(data[m_data_key]["temperature"][0])
        new_data[m_data_key]["temperature"] = new_data[m_data_key]["temperature"][1:61]
        new_data[m_data_key]["speed"].append(data[m_data_key]["speed"][0])
        new_data[m_data_key]["speed"] = new_data[m_data_key]["speed"][1:61]
        new_data[m_data_key]["latitude"].append("{0:09.4f}".format(gps_minute_file["lat"][(60 + interval) % 3600]))
        new_data[m_data_key]["latitude"] = new_data[m_data_key]["latitude"][1:61]
        new_data[m_data_key]["longitude"].append("{0:09.4f}".format(gps_minute_file["lon"][(60 + interval) % 3600]))
        new_data[m_data_key]["longitude"] = new_data[m_data_key]["longitude"][1:61]

        new_data[m_data_key]["fuel"].append(data[m_data_key]["fuel"][0])
        new_data[m_data_key]["fuel"] = new_data[m_data_key]["fuel"][1:61]
        new_data[m_data_key]["battery"].append(data[m_data_key]["battery"][0])
        new_data[m_data_key]["battery"] = new_data["minute_data_0"]["battery"][1:61]

        if interval % 60000 == 0:
            new_data[h_data_key]["elevation"].append(data[h_data_key]["elevation"][0])
            new_data[h_data_key]["elevation"] = new_data[h_data_key]["elevation"][1:61]
            new_data[h_data_key]["temperature"].append(data[h_data_key]["temperature"][0])
            new_data[h_data_key]["temperature"] = new_data[h_data_key]["temperature"][1:61]
            new_data[h_data_key]["speed"].append(data[h_data_key]["speed"][0])
            new_data[h_data_key]["speed"] = new_data[h_data_key]["speed"][1:61]
            new_data[h_data_key]["latitude"].append("{0:09.4f}".format(gps_hour_file["lat"][interval % 60]))
            new_data[h_data_key]["latitude"] = new_data[h_data_key]["latitude"][1:61]
            new_data[h_data_key]["longitude"].append("{0:09.4f}".format(gps_hour_file["lon"][interval % 60]))
            new_data[h_data_key]["longitude"] = new_data[h_data_key]["longitude"][1:61]
            new_data[h_data_key]["fuel"].append(data[h_data_key]["fuel"][0])
            new_data[h_data_key]["fuel"] = new_data[h_data_key]["fuel"][1:61]
            new_data[h_data_key]["battery"].append(data[h_data_key]["battery"][0])
            new_data[h_data_key]["battery"] = new_data[h_data_key]["battery"]

    return new_data


# Callbacks Dropdown


@dash.callback(
    Output("satellite-name", "children"),
    [Input("satellite-dropdown-component", "value")],
)
def update_satellite_name(val):
    if val == "h45-k1":
        return "Satellite\nH45-K1"
    elif val == "l12-5":
        return "Satellite\nL12-5"
    else:
        return ""


@dash.callback(
    Output("satellite-description", "children"),
    [Input("satellite-dropdown-component", "value")],
)
def update_satellite_description(val):
    text = "Select a mnkhal to view using the dropdown above."

    if val == "Mnkhal 1":
        text = (
            "Mnkhal, also known as MK IIR-9 and MK SVN-45, is an coffee beans filter device which forms part "
            "of the Global Positioning System."
        )

    elif val == "Mnkhal 2":
        text = (
            "The coffee bean filter, designed for high precision, is an advanced machine that detects impurities such as stones, leaves, and dust in coffee beans. Utilizing cutting-edge technology, this filter ensures that only the purest beans make it through. It operates by scanning the beans as they pass through, identifying and removing any foreign particles with pinpoint accuracy. The system is robust and reliable, built to handle large quantities of beans while maintaining high standards of quality and safety. This innovation marks a significant step forward in coffee processing, ensuring a superior product for consumers."
        )
    return text


# Callbacks Components


@dash.callback(Output("control-panel-time-now-component", "value"), [Input("interval", "n_intervals")])
def update_time(interval):
    now = time.time()
    local_time = time.localtime(now)
    hours = local_time.tm_hour
    minutes = int((now % 3600) // 60)
    seconds = int(now % 60)

    # Format the time as HH:MM:SS
    return f"{hours:02}:{minutes:02}:{seconds:02}"


@dash.callback(
    Output("control-panel-running-time-component", "value"),
    Input("interval", "n_intervals"),
    State("tooltips-toggle", "on"),
    prevent_initial_call=True
)
def update_running_time(n_intervals, switch_toggle):
    global start_time, running_seconds

    if switch_toggle:
        if start_time == 0:  # if counter just started
            start_time = time.time()  # set the current time as the start time
        running_seconds = time.time() - start_time  # calculate the elapsed time
    else:
        running_seconds = 0  # reset running time when switch is off
        start_time = 0  # reset start time

    # Convert running seconds to hours, minutes, and seconds
    hours = int(running_seconds // 3600)
    minutes = int((running_seconds % 3600) // 60)
    seconds = int(running_seconds % 60)

    # Format the time as HH:MM:SS
    return f"{hours:02}:{minutes:02}:{seconds:02}"


@dash.callback(
    [
        Output("control-panel-elevation-component", "value"),
        Output("control-panel-temperature-component", "value"),
        Output("control-panel-speed-component", "value"),
        Output("control-panel-fuel-component", "value"),
        Output("control-panel-battery-component", "value"),
    ],
    [Input("interval", "n_intervals"), Input("satellite-dropdown-component", "value")],
    [State("store-data-config", "data"), State("store-data", "data")],
)
def update_non_gps_component(clicks, satellite_type, data_config, data):
    string_buffer = ""
    if data_config["satellite_type"] == 0:
        string_buffer = "_0"
    if data_config["satellite_type"] == 1:
        string_buffer = "_1"

    new_data = []
    components_list = ["elevation", "temperature", "speed", "fuel", "battery"]
    # Update each graph value
    for component in components_list:
        new_data.append(data["minute_data" + string_buffer][component][-1])

    return new_data


@dash.callback(
    [
        Output("control-panel-latitude-component", "value"),
        Output("control-panel-longitude-component", "value"),
    ],
    [Input("interval", "n_intervals"), Input("satellite-dropdown-component", "value")],
    [State("store-data-config", "data"), State("store-data", "data")],
)
def update_gps_component(clicks, satellite_type, data_config, data):
    string_buffer = ""
    if data_config["satellite_type"] == 0:
        string_buffer = "_0"
    if data_config["satellite_type"] == 1:
        string_buffer = "_1"

    new_data = []
    for component in ["latitude", "longitude"]:
        val = list(data["minute_data" + string_buffer][component][-1])
        if val[0] == "-":
            new_data.append("0" + "".join(val[1::]))
        else:
            new_data.append("".join(val))
    return new_data


@dash.callback(
    [
        Output("control-panel-latitude-component", "color"),
        Output("control-panel-longitude-component", "color"),
    ],
    [Input("interval", "n_intervals"), Input("satellite-dropdown-component", "value")],
    [State("store-data-config", "data"), State("store-data", "data")],
)
def update_gps_color(clicks, satellite_type, data_config, data):
    string_buffer = ""
    if data_config["satellite_type"] == 0:
        string_buffer = "_0"
    if data_config["satellite_type"] == 1:
        string_buffer = "_1"

    new_data = []

    for component in ["latitude", "longitude"]:
        value = float(data["minute_data" + string_buffer][component][-1])
        if value < 0:
            new_data.append("#ff8e77")
        else:
            new_data.append("#fec036")

    return new_data


@dash.callback(
    # Output("control-panel-communication-signal", "value"),
    Output('control-panel-communication-signal', 'color'),
    [Input("interval", "n_intervals")],
)
def update_communication_component(clicks):
    return '#00FF00' if clicks % 2 == 0 else '#fec036'

@dash.callback(
    Output(component_id='tooltips-toggle', component_property='label'),
    Input(component_id='tooltips-toggle', component_property='on')
)
def update_switch_toggle_info(tooltips_toggle):
    return 'Device is On' if tooltips_toggle else 'Device is Off'

@dash.callback(
    Output("control-panel-weight-component", "value"),
    [Input("interval", "n_intervals"),
     Input('tooltips-toggle', 'on')],
)
def update_weight_info(interval, switch_toggle_value):
    global current_weight
    if current_weight >= 50 or switch_toggle_value is False:
        current_weight = 0
    else:
        current_weight = current_weight + random.uniform(0, 5) if interval % 3 == 0 else current_weight
    return "{:.2f}".format(current_weight)

@dash.callback(
    Output("control-panel-vibration-component", "value"),
    [Input("interval", "n_intervals"),
     Input('tooltips-toggle', 'on')],
)
def update_vaibration_component(interval, switch_toggle_value):
    if switch_toggle_value and interval % 5 == 0:
        new_value = current_vibration + random.uniform(-2, 2)
    elif switch_toggle_value:
        new_value = current_vibration
    else:
        new_value = 0
    return "{:.2f}".format(new_value)

@dash.callback(
    Output('control-panel-camera', 'color'),
    Input('tooltips-toggle', 'on')
)
def update_camera_color(switch_toggle_value):
    return '#00FF00' if switch_toggle_value else '#FF0000'

@dash.callback(
    Output("control-panel-fan-speed-component", "value"),
    [
        Input("interval", "n_intervals"),
        Input('tooltips-toggle', 'on')
    ],
)
def update_fan_speed_component(interval, switch_toggle_value):
    if switch_toggle_value:
        return 27.859 + random.uniform(-2, 2)
    else:
        return 0


####################### PAGE LAYOUT #############################
layout = root_layout
