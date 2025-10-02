from dash import html, dcc
import datetime
from dataLoader import get_dropdown_options
from dataLoader import get_files_in_folder
from dataLoader import GRAPH_FOLDER
from styles.Colors import *
from styles.Styles import *

buttons = get_files_in_folder(GRAPH_FOLDER)

def create_layout():
    column_data = get_dropdown_options()

    buttons = ["Check in Emotions", "Check in Levels",
               "Monthly First Downs", "Monthly Sacks", "Year-Over-Year First Downs", "Year-Over-Year Sacks"]

    return html.Div([
        html.H1('Fight For Life Report Generator', style={'textAlign': "center", 'color':DEEP_BLUE}),  # Title
        dcc.Download(id='download-pdf'),
        dcc.Store(id='selected-graphs', data=[]),
        html.Div([  # Whole div
            html.Div([  # Left side menu div
                html.Div([  # Buttons div
                    dcc.Dropdown(
                        id='dropdown-menu',  # Unique ID for the dropdown
                        options=[{'label': item, 'value': item} for item in column_data],
                        value=column_data[0],  # Set default value to the first entry in the column
                        clearable=False,  # Prevents the user from clearing the selection
                        style={**dropdown_style}
                    ),
                    dcc.DatePickerSingle(
                        id='month-picker',  # Unique ID for the picker
                        date='2022-10-01',  # Current date
                        display_format='YYYY-MM',  # Display format to show the month and year
                        style={**dropdown_style}
                    ),
                ], style={
                    "display": "flex",
                    "justifyContent": "center",
                    "alignItems": "center",
                    "gap": "20px"
                }),

                html.Div(id='selected-graph-names', style={ 'color': 'black', 'padding': '15px', 'fontFamily': font_family, 'font-size': '14px'}),

                html.Div([  # Graph grid
                    *[html.Button(button, id=f"button-{i}", n_clicks=0, style=graph_selection_style)  # Pass individual button name
                    for i, button in enumerate(buttons)]  # Loop through the list to create buttons
                ], style={
                    "display": "grid",  # Use grid layout
                    "gridTemplateColumns": "repeat(2, 1fr)",  # 2 equal columns
                    "gridAutoRows": "minmax(100px, auto)",  # Automatically adjust row height
                    "gap": "10px",
                }),

                html.Div(  # Text area div
                    dcc.Textarea(
                        id="text-area",
                        placeholder="Type something...",
                        style=text_box_style
                    ),
                    style={
                        "padding": "15px",  # Adds space around the entire textarea
                        "backgroundColor": "#f8f8f8",  # Optional: Light background to enhance padding effect
                        "borderRadius": "12px",  # Matches textarea for consistency
                    }
                ),

                # Display the selected option from dropdown-menu
                html.Div(id='output-container'),

                # Button to generate the graph
                html.Button(
                    "Update Graph",
                    id="run-command-button",
                    n_clicks=0,
                    style=button_style
                ),

                html.Div(
                    id="button-space",
                    style={'padding': '5px'}
                ),



                html.Button(
                    "Export",
                    id="export-button",
                    n_clicks=0,
                    style=button_style,
                ),
            ], style={"background": "white", 'flex': 1, 'padding': '20px'}),  # Flex at 1 keeps the columns the same length as each other

            html.Div([  # Right preview data div
                html.Img(id="graph-image", style={
                    "maxWidth": "48vw",   # Maximum width 48% of the screen
                    "objectFit": "contain"  # Ensures the image maintains its aspect ratio
                }),
            ], style={
                "background": WHITE, 
                "display": "flex",  # Make the div a flex container
                "justifyContent": "center",  # Center horizontally
                "alignItems": "center",  # Center vertically
                "flex": 1  # Ensure it takes up remaining space
            })
        ], style={
            "display": "flex",  # 2 columns
            "gap": "10px",
            "background": DEEP_BLUE,
            "padding": "10px",
        })
    ])
