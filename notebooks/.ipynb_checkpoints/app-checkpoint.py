import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import pickle 
from dash.dependencies import Input, Output

# Change the file path
# with open(args.model, 'rb') as f:
#         model = pkl.load(f)
        
app = dash.Dash(__name__,)

app.layout = html.Div(children=[
    html.H4(children='Fraud Detector'),
    dcc.Input(id='my-input', value='Feature 1', type='text'),
    dcc.Input(id='my-input2', value='Feature 2', type='text'),
    dcc.Input(id='my-input3', value='Feature 3', type='number'),
    html.Div(id='my-output')
])


@app.callback(
    Output("my-output", "children"),
    Input("my-input", "value"),
    Input("my-input2", "value"),
    Input("my-input3", "value"),
)
def prediction(inp1,inp2,inp3):
    p = model.predict(inp1,inp2,inp3)
    return "Result: {}".format(p)


if __name__ == '__main__':
    app.run_server(debug=True)