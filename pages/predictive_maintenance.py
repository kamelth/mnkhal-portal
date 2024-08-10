import pandas as pd
import dash
from dash import dcc, html, callback
import plotly.express as px
from dash.dependencies import Input, Output
import plotly.graph_objects as go

dash.register_page(__name__, path='/predictive-maintenance', name="Predictive Maintenance 📈")

####################### DATASET #############################
df = pd.read_csv("final_coffee_machine_data.csv")

####################### LIMITS #############################
vibration_limit = (29, 31)  # Example limits for vibration level (Hz)
fan_speed_limit = (20, 30)  # Example limits for fan speed (RPM)

mean_weight = df['Weight'].mean()
ucl_weight = 20
lcl_weight = 40

# Page layout with two rows of graphs
layout = html.Div(children=[
    # Interval component to refresh graphs every 5 seconds
    dcc.Interval(id="interval-component", interval=5*1000, n_intervals=0),

    # First row with two graphs
    html.Div(children=[
        dcc.Graph(id="filtered-weight-control-chart"),
        dcc.Graph(id="camera-status-treemap")
    ], style={'display': 'flex', 'flex-direction': 'row'}),
    
    # Second row with two graphs
    html.Div(children=[
        dcc.Graph(id="vibration-level-check"),
        dcc.Graph(id="fan-speed-check")
    ], style={'display': 'flex', 'flex-direction': 'row'})
])

# Callback for the first graph: Control Chart for Filtered_Weight
@callback(Output("filtered-weight-control-chart", "figure"), [Input("interval-component", "n_intervals")])
def update_control_chart(n_intervals):
    fig = go.Figure()

    # Add the Filtered_Weight data
    fig.add_trace(go.Scatter(x=df['Timestamp'], y=df['Weight'], mode='lines+markers', name='Filtered Weight'))

    # Add the mean line
    fig.add_trace(go.Scatter(x=df['Timestamp'], y=[mean_weight]*len(df), mode='lines', name='Mean', line=dict(color='green', dash='dash')))

    # Add the upper control limit line
    fig.add_trace(go.Scatter(x=df['Timestamp'], y=[ucl_weight]*len(df), mode='lines', name='Upper Control Limit (UCL)', line=dict(color='red', dash='dash')))

    # Add the lower control limit line
    fig.add_trace(go.Scatter(x=df['Timestamp'], y=[lcl_weight]*len(df), mode='lines', name='Lower Control Limit (LCL)', line=dict(color='red', dash='dash')))

    fig.update_layout(title="Control Chart for Filtered Weight", xaxis_title="Timestamp", yaxis_title="Filtered Weight (kg)")
    
    return fig

# Callback for the second graph: Treemap for Camera_Status
@callback(Output("camera-status-treemap", "figure"), [Input("interval-component", "n_intervals")])
def update_camera_status_histogram(n_intervals):
    fig = go.Figure()

    # Add the Filtered_Weight data
    fig.add_trace(go.Scatter(x=df['Hour'], y=df['Weight'], mode='markers', name='Filtered Weight'))

    # Add the mean Hour
    # fig.add_trace(go.Scatter(x=df['Hour'], y=[mean_weight]*len(df), mode='lines', name='Mean', line=dict(color='green', dash='dash')))

    # Add the upper control limit line
    # fig.add_trace(go.Scatter(x=df['Hour'], y=[ucl_weight]*len(df), mode='lines', name='Upper Control Limit (UCL)', line=dict(color='red', dash='dash')))

    # Add the lower control limit line
    # fig.add_trace(go.Scatter(x=df['Hour'], y=[lcl_weight]*len(df), mode='lines', name='Lower Control Limit (LCL)', line=dict(color='red', dash='dash')))

    fig.update_layout(title="Filtered Weight in every hours", xaxis_title="Hour", yaxis_title="Filtered Weight (kg)")
    
    return fig

# Callback for the third graph: Vibration_Level issues over time (aggregated by hour)
# Callback for the fourth graph: Fan_Speed check over time
@callback(Output("vibration-level-check", "figure"), [Input("interval-component", "n_intervals")])
def update_fan_speed_chart(n_intervals):
    df['Vibration_Level_Issue'] = (df['Vibration_Level'] < vibration_limit[0]) | (df['Vibration_Level'] > vibration_limit[1])
    
    fig = px.scatter(df, x='Timestamp', y='Vibration_Level', color='Vibration_Level_Issue',
                     title="Vibration Level vs Time (Out of Limits)",
                     labels={'Vibration_Level_Issue': 'Vibration Level Issue'})
    return fig

# Callback for the fourth graph: Fan_Speed check over time
@callback(Output("fan-speed-check", "figure"), [Input("interval-component", "n_intervals")])
def update_fan_speed_chart(n_intervals):
    df['Fan_Speed_Issue'] = (df['Fan_Speed'] < fan_speed_limit[0]) | (df['Fan_Speed'] > fan_speed_limit[1])
    
    fig = px.scatter(df, x='Timestamp', y='Fan_Speed', color='Fan_Speed_Issue',
                     title="Fan Speed vs Time (Out of Limits)",
                     labels={'Fan_Speed_Issue': 'Fan Speed Issue'})
    return fig