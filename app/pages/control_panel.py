import dash
import time
import pathlib
import random
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import State, Input, Output
import dash_daq as daq
import paho.mqtt.client as paho
import sys
import json
import threading
import socket


mosquitto_ip = socket.gethostbyname('mosquitto')
print(f"Mosquitto Broker IP Address: {mosquitto_ip}")

current_weight = 0
current_vibration = 0

def onMessage(client, userData, msg):
    global current_weight, current_vibration

    data = json.loads(msg.payload.decode())
    current_weight = data.get('weight', 0)
    current_vibration = data.get('vibration', 0)
    print(f"Weight: {current_weight}, Vibration: {current_vibration}")


def mqtt_client_thread():
    client = paho.Client()
    client.on_message = onMessage

    if client.connect(mosquitto_ip, 1883, 60) != 0:
        print('Couldn\'t connect to MQTT Broker!')
        sys.exit(-1)

    client.subscribe('test/sensors')

    try:
        print('MQTT Client Running...')
        client.loop_forever()  # This will run in the background
    except Exception as e:
        print(f'Disconnecting from Broker: {e}')
        client.disconnect()


# Create and start the MQTT thread
mqtt_thread = threading.Thread(target=mqtt_client_thread)
mqtt_thread.daemon = True  # Set as a daemon thread so it exits with the main program
mqtt_thread.start()

dash.register_page(__name__, path="/", name="Control Panel 🎛️")

# Initialize a global variable to store the running time
start_time = time.time() - random.randint(0, 172800)
running_seconds = 0


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

camera = daq.Indicator(
    className="panel-lower-indicator",
    id="control-panel-camera",
    label="Camera",
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

# Histogram

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

# Root
root_layout = html.Div(
    id="root",
    children=[
        # For the case no components were clicked, we need to know what type of graph to preserve
        dcc.Store(id="store-data-config", data={"info_type": "", "satellite_type": 0}),
        side_panel_layout,
        main_panel_layout,
    ],
)


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
    return "{:.2f}".format(current_weight)

@dash.callback(
    Output("control-panel-vibration-component", "value"),
    [Input("interval", "n_intervals"),
     Input('tooltips-toggle', 'on')],
)
def update_vaibration_component(interval, switch_toggle_value):
    return "{:.2f}".format(current_vibration)


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
