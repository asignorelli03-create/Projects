from styles.Colors import *

font_family = "'Arial', 'sans-serif'"  # Define the font family

button_style = {
    'backgroundColor': DEEP_BLUE,
    'color': WHITE,
    'border': 'none',
    'padding': '15px 32px',
    'textAlign': 'center',
    'textDecoration': 'none',
    'display': 'inline-block',
    'fontSize': '16px',
    'cursor': 'pointer',
    'borderRadius': '12px',
    'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)',
    'fontFamily': font_family
}

date_picker_style = {
    'backgroundColor': WHITE,
    'color': DARK_GRAY,
    'border': f'1px solid {LIGHT_GRAY}',
    'borderRadius': '8px',
    'padding': '10px',
    'fontSize': '16px',
    'width': '200px',
    'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)',
    'cursor': 'pointer',
    'transition': 'all 0.3s ease',
    'fontFamily': font_family
}

text_box_style = {
    'width': '100%',
    'height': '120px',
    'borderRadius': '10px',
    'border': '2px solid #ccc',
    'padding': '10px',
    'fontSize': '16px',
    'boxShadow': '0 2px 5px rgba(0, 0, 0, 0.1)',
    'transition': 'all 0.3s ease',
    'outline': 'none',
    'fontFamily': font_family  
}

dropdown_style = {
    'backgroundColor': WHITE,
    'color': DARK_GRAY,
    'minWidth': '200px',
    'minHeight': '50px',
    'padding': '10px',
    'borderRadius': '8px',
    'border': f'1px solid {DARK_GRAY}',
    'boxShadow': '0 4px 10px rgba(0, 0, 0, 0.15)',
    'zIndex': '1',
    'position': 'relative',
    'margin': '.5px',
    'transition': 'all 0.3s ease',
    'fontFamily': font_family 
}

dropdown_item_style = {
    'padding': '12px 18px',
    'textDecoration': 'none',
    'color': DARK_GRAY,
    'display': 'block',
    'cursor': 'pointer',
    'transition': 'background-color 0.3s ease',
    'fontFamily': font_family  
}

dropdown_item_hover_style = {
    'backgroundColor': LIGHT_GRAY,
    'color': DARK_GRAY,
    'borderRadius': '4px',
    'fontFamily': font_family  
}

dropdown_focused_style = {
    'borderColor': GROWTH_GREEN,
    'boxShadow': f'0 0 5px 2px {GROWTH_GREEN}',
    'fontFamily': font_family  
}

graph_selection_style = {
    'backgroundColor': GROWTH_GREEN,
    'color': DEEP_BLUE,
    'border': 'none',
    'padding': '15px 32px',
    'fontWeight': 'bold',
    'textAlign': 'center',
    'textDecoration': 'none',
    'display': 'inline-block',
    'fontSize': '16px',
    'cursor': 'pointer',
    'borderRadius': '12px',
    'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)',
    'fontFamily': font_family  
}