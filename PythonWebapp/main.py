import dash
from flask import Flask
from layout import create_layout
from callbacks import register_callbacks

# Initialize Flask server
server = Flask(__name__)
app = dash.Dash(__name__, server=server)

# Set the layout
app.layout = create_layout()

# Register callbacks
register_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=True)
