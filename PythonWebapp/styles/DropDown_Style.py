from styles.Colors import (GROWTH_GREEN, DEEP_BLUE, WHITE,
    FFL_BLACK, EXPLORE_YELLOW, BRONZE, INSPIRE_RED, LIGHT_GRAY, DARK_GRAY)

dropdown_style = {
    'backgroundColor': WHITE,  # White background for dropdown
    'color': DARK_GRAY,  # Text color for dropdown
    'minWidth': '160px',  # Minimum width for the dropdown
    'padding': '8px',  # Padding inside the dropdown
    'borderRadius': '8px',  # Rounded corners
    'boxShadow': '0 8px 16px rgba(0, 0, 0, 0.2)',  # Shadow for the dropdown
    'zIndex': '1',  # Ensure it's above other elements
    'position': 'relative',  # Positioning relative to its parent container
    'margin': '20px',  # Adding margin around the dropdown
}

dropdown_item_style = {
    'padding': '12px 16px',  # Padding for dropdown items
    'textDecoration': 'none',  # No underline on items
    'color': DARK_GRAY,  # Text color for items
    'display': 'block',  # Block display to take up full width
    'cursor': 'pointer',  # Pointer cursor on hover
}

# Hover effect for dropdown items
dropdown_item_hover_style = {
    'backgroundColor': LIGHT_GRAY,  # Change background on hover
}
