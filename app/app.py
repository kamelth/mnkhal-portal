from dash import Dash, html, dcc
import dash
import plotly.express as px

px.defaults.template = "ggplot2"

external_css = ["https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css", ]

app = Dash(__name__, pages_folder='pages', use_pages=True, external_stylesheets=external_css, suppress_callback_exceptions=True)

app.layout = html.Div([
	html.Br(),
	html.P('Mnkhal Web Portal', className="text-center fw-bold fs-1", style={'color': '#fec036'}),
    html.Div(children=[
	    dcc.Link(page['name'], href=page["relative_path"], className="btn btn-dark m-2 fs-5")\
			  for page in dash.page_registry.values()]
	),
	dash.page_container
], className="col-12 mx-auto")

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8050, debug=True)