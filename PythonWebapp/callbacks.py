from dash import Input, Output, State, ctx, callback,dcc
import os
import base64
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.backends.backend_pdf import PdfPages  # ✅ Ensure PdfPages is imported
from graphs import Monthly_Sacks as ms
from graphs import Monthly_First_Downs as mfd
from graphs import Check_In_Emotions as cie
from graphs import Check_In_Levels as cil
from graphs import YoY_FD  as yoyfd
from graphs import YoY_Sacks as yoys
from styles.Styles import *
from styles.Colors import DEEP_BLUE
import os
import io
from PIL import Image
import numpy as np
import textwrap
import dash
GRAPH_FOLDER = os.path.join(os.getcwd(), "graphs")
DATA_FOLDER = os.path.join(os.getcwd(), "data")



def register_callbacks(app):
    @app.callback(
        [Output('graph-image', 'src'),
        Output('output-container', 'children')],
        [Input('run-command-button', 'n_clicks'),
         Input('month-picker', 'date'),
        Input('dropdown-menu', 'value')],
        [State('text-area', 'value'),
        State('selected-graphs', 'data')],
        )
    def run_command(n_clicks, date, classroom, summarytxt, selected_graphs):
        print(f"n_clicks: {n_clicks}, date: {date}, classroom: {classroom}, summarytxt: {summarytxt}, selected_graphs: {selected_graphs}")
        if summarytxt is None:
            summarytxt = ""
        if n_clicks > 0:  # Check if the button was clicked
            
            graph_path = os.path.join(DATA_FOLDER, "graph.pdf")  # Relative path  # Ensure this path is writable



            # Set figure size (in inches)
            figure_width = 816  # Convert from pixels to inches
            figure_height = 1056  # Convert from pixels to inches

            # Create figure with the specified size
            fig, axs = plt.subplots(2, 2, figsize=(figure_width/100, figure_height/100))

            for ax in axs.flat:
                ax.set_visible(False)  # Hide all subplot axes initially


            # Add custom axes for graphs
            
            custom_axes = [
                fig.add_axes([16/figure_width+40/figure_width, 390/figure_height+60/figure_height,386/figure_width-40/figure_width , 264/figure_height+20/figure_height]),
                fig.add_axes([424/figure_width+40/figure_width, 390/figure_height+60/figure_height, 386/figure_width-40/figure_width , 264/figure_height+20/figure_height]),
                fig.add_axes([16/figure_width+40/figure_width, 10/figure_height+40/figure_height, 386/figure_width-40/figure_width , 264/figure_height+20/figure_height]),
                fig.add_axes([424/figure_width+40/figure_width, 10/figure_height+40/figure_height,386/figure_width -40/figure_width, 264/figure_height+20/figure_height])
            ]
            figure_width = 816/100  # Convert from pixels to inches
            figure_height = 1056/100

            if not selected_graphs or len(selected_graphs) == 0:
                return "", "Please select up to 4 graphs before generating."

            graph_dropdowns = selected_graphs[:4]

            #data = "Ms. Rowley's Class"
            data = classroom

            if date is not None:
                year = date[:4]
                month = date[5:7]
                month = 9
                year = 2021
                for graph_type, ax in zip(graph_dropdowns, custom_axes):  # Unpack tuple properly
                    if graph_type == "Monthly Sacks":
                        ms.createGraph(ax,month,year,data)  
                    if graph_type == "Monthly First Downs":
                        mfd.createGraph(ax,month,year,data)
                    if graph_type == "Check in Emotions":
                        cie.createGraph(ax,month,year)  
                    if graph_type == "Check in Levels":
                        cil.createGraph(ax,month,year)
                    if graph_type == "Year-Over-Year First Downs":
                        yoyfd.createGraph(ax, month,year, data)
                    if graph_type == "Year-Over-Year Sacks":
                        yoys.createGraph(ax, month,year, data)



            
            #top blue bar
            top_banner_ax = fig.add_axes([0, 0.947, 1, 0.053])  # Adjust size and position

            # Style the blue bar
            top_banner_ax.set_facecolor(DEEP_BLUE)  # Set background color
            top_banner_ax.set_xticks([])  # Remove x ticks
            top_banner_ax.set_yticks([])  # Remove y ticks
            top_banner_ax.spines["top"].set_visible(False)  # Hide top spine
            top_banner_ax.spines["bottom"].set_visible(False)  # Hide bottom spine
            top_banner_ax.spines["left"].set_visible(False)  # Hide left spine
            top_banner_ax.spines["right"].set_visible(False)  # Hide right spine

            # Add text to the blue bar
            top_banner_ax.text(
                0.5, 0.5,  # Position (centered)
                classroom +"      "+date,  # Text
                fontsize=16, color="white", weight="bold",  # Style
                ha="center", va="center",  # Align text
                transform=top_banner_ax.transAxes  # Keep position fixed relative to the axis
            )

            bottom_banner_ax = fig.add_axes([0, -0.0854, 1, 0.053])

            bottom_banner_ax.set_facecolor(DEEP_BLUE)
            bottom_banner_ax.set_xticks([])
            bottom_banner_ax.set_yticks([])
            bottom_banner_ax.spines["top"].set_visible(False)
            bottom_banner_ax.spines["bottom"].set_visible(False)
            bottom_banner_ax.spines["left"].set_visible(False)
            bottom_banner_ax.spines["right"].set_visible(False)

            bottom_banner_ax.text(
                0.5, 0.5,
                "contact information",
                fontsize=16, color="white", weight="bold",
                ha="center", va="center",
                transform=bottom_banner_ax.transAxes
            )



            # Move paragraph text box 20 pixels higher
            paragraph_ax = fig.add_axes([0.20, 0.781 - .03, 0.70, 0.101])  # Adjust y position to move it up
            paragraph_ax.set_facecolor(WHITE)
            paragraph_ax.set_xticks([])
            paragraph_ax.set_yticks([])
            paragraph_ax.spines["top"].set_visible(False)
            paragraph_ax.spines["bottom"].set_visible(False)
            paragraph_ax.spines["left"].set_visible(False)
            paragraph_ax.spines["right"].set_visible(False)

            wrapped_text = textwrap.fill(summarytxt, width=80)

            paragraph_ax.text(
                0, 1,
                wrapped_text,
                fontsize=14, color=DEEP_BLUE, weight="normal",
                ha="left", va="top",
                fontname="Arial",
                transform=paragraph_ax.transAxes
            )


            #title at 350,300 - 1400,190
            title_ax = fig.add_axes([0.23,0.850,0.70,0.065])
            title_ax.set_facecolor("none")
            title_ax.set_xticks([])
            title_ax.set_yticks([])
            title_ax.spines["top"].set_visible(False)  # Hide top spine
            title_ax.spines["bottom"].set_visible(False)  # Hide bottom spine
            title_ax.spines["left"].set_visible(False)  # Hide left spine
            title_ax.spines["right"].set_visible(False) 

            title_ax.text(0.28, 0.5, "BUILDING DREAMS", fontsize=22, color=DEEP_BLUE, weight="heavy", ha="center", va="center", transform=title_ax.transAxes)
            title_ax.text(0.80, 0.5, "AT-A-GLANCE", fontsize=22, color=GROWTH_GREEN, weight="heavy", ha="center", va="center", transform=title_ax.transAxes)


            #pic 90 820
            picture_ax = fig.add_axes([0.0177, 0.725, 0.1825, 0.2425])
            picture_ax.set_facecolor(WHITE)
            picture_ax.set_xticks([])
            picture_ax.set_yticks([])
            picture_ax.spines["top"].set_visible(False)  # Hide top spine
            picture_ax.spines["bottom"].set_visible(False)  # Hide bottom spine
            picture_ax.spines["left"].set_visible(False)  # Hide left spine
            picture_ax.spines["right"].set_visible(False) 
             # Ensure the image is in the correct path

            GRAPH_FOLDER = os.path.join(os.getcwd(), "data") 
            logo_path = os.path.join(DATA_FOLDER, "logo.png")

            img = mpimg.imread(logo_path)
            picture_ax.imshow(img)


            #background color
            fig.patch.set_facecolor(WHITE)



            fig.savefig(graph_path, format="png", bbox_inches='tight', dpi=100)  # Save as PNG
            plt.close(fig)
            # Convert image to base64
            with open(graph_path, "rb") as img_file:
                encoded_image = base64.b64encode(img_file.read()).decode()

            img_src = f"data:image/png;base64,{encoded_image}"

            return img_src, "Graph updated"

        return "","Click the button to create the graph."
    
        



    graph_names = ["Check in Emotions", "Check in Levels",
               "Monthly First Downs", "Monthly Sacks", "Year-Over-Year First Downs", "Year-Over-Year Sacks"]


    @app.callback(
        [Output('selected-graphs', 'data')] +
        [Output(f'button-{i}', 'style') for i in range(len(graph_names))] +
        [Output('selected-graph-names', 'children')],
        [Input(f'button-{i}', 'n_clicks') for i in range(len(graph_names))],
        State('selected-graphs', 'data'),
        prevent_initial_call=True
    )
    def update_selected_graphs(*args):
        clicks = args[:-1]
        selected_graphs = args[-1] or []

        changed_id = ctx.triggered_id
        if changed_id is not None:
            index = int(changed_id.split("-")[1])
            graph_clicked = graph_names[index]

            if graph_clicked in selected_graphs:
                selected_graphs.remove(graph_clicked)
            else:
                if len(selected_graphs) < 4:
                    selected_graphs.append(graph_clicked)

        # Define style for selected and unselected
        selected_style = {
            **graph_selection_style,
            "backgroundColor": DEEP_BLUE,
            "color": "white",
            "border": "2px solid #1f5fd3"
        }
        unselected_style = graph_selection_style

        styles = [selected_style if graph_names[i] in selected_graphs else unselected_style for i in range(len(graph_names))]

        # Generate display text
        if selected_graphs:
            selected_text = "Selected Graphs: " + ", ".join(selected_graphs)
        else:
            selected_text = "No graphs selected."

        return [selected_graphs] + styles + [selected_text]
    
    @app.callback(
        Output("download-pdf", "data"),
        Input("export-button", "n_clicks"),
        Input('month-picker', 'date'),
        Input('dropdown-menu', 'value'),
        State("graph-image", "src"),
        prevent_initial_call=True
    )
    def export_pdf(n_clicks,date,classroom, image_src):
        if not image_src or not image_src.startswith("data:image"):
            return dash.no_update

        # Extract base64 data from the src string
        header, encoded = image_src.split(",", 1)
        img_data = base64.b64decode(encoded)

        # Open image from bytes
        image = Image.open(io.BytesIO(img_data))

        # Convert to numpy array for matplotlib
        image_np = np.array(image)

        # Create PDF with matplotlib
        fig, ax = plt.subplots(figsize=(8, 6))
        fig.patch.set_facecolor('#B8D432')
        ax.imshow(image_np)
        ax.axis('off')

        buf = io.BytesIO()
        with PdfPages(buf) as pdf:
            pdf.savefig(fig)
        plt.close(fig)
        buf.seek(0)

        return dcc.send_bytes(buf.read(), filename=date+":"+classroom+".pdf")


        
        