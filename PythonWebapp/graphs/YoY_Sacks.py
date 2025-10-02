import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import calendar
from matplotlib.backends.backend_pdf import PdfPages
from styles.Colors import (GROWTH_GREEN, DEEP_BLUE, WHITE, FFL_BLACK, EXPLORE_YELLOW, BRONZE, INSPIRE_RED, LIGHT_GRAY, DARK_GRAY)
import os

def createGraph(ax,monthNum,yearNum,classroom):

    GRAPH_FOLDER = os.path.join(os.getcwd(), "data")
    CSV_FILE_PATH = os.path.join(GRAPH_FOLDER, "testdata.csv")
    df = pd.read_csv(CSV_FILE_PATH)
    df['dateTime'] = pd.to_datetime(df['dateTime'])
    
    # Set the current year manually for the database
    current_year = int(yearNum)
    monthNum = int(monthNum)
    # Define the range for August and September of this year and last year
    lastMonth = f"{int(monthNum) - 1:02d}"
    thisMonth = f"{int(monthNum) :02d}"
    date_range = [f'{current_year-1}-{lastMonth}',
                f'{current_year-1}-{thisMonth}',
                f'{current_year}-{lastMonth}',
                f'{current_year}-{thisMonth}']

    # Create a list to store the counts for each month
    play_counts = []

    # Loop through each month and count play entries
    for date_prefix in date_range:
        # Filter the DataFrame for the specific month
        filtered_df = df[(df['type'] == "Sack") & 
                 (df['dateTime'].dt.strftime('%Y-%m') == date_prefix) & 
                 (df['classrooms_text'] == classroom)]
 
        # Append the count to the list
        play_counts.append(filtered_df.shape[0])

    # Swap the second and third items in the list (index 1 and 2)
    play_counts[1], play_counts[2] = play_counts[2], play_counts[1]

    # Sample data
    data = {
        'Proportion': [.25,.25,.75,.75],
        'Plays': play_counts,
        'Line': ['Last School Year', 'This School Year', 'Last School Year', 'This School Year']
    }

    # Convert to DataFrame
    df = pd.DataFrame(data)

    # Set up the plot
    sns.lineplot(
        ax=ax,
        x='Proportion',
        y='Plays',
        hue='Line',
        style='Line',
        data=df,
        markers=True,
        dashes=False,
        palette=[GROWTH_GREEN, DEEP_BLUE],
        markeredgecolor=FFL_BLACK,
        linewidth=2.5
    )
    
    ax.grid(True)

    # Customize the legend
    ax.legend_.remove() 
    ax.text(0.15, 1.05, 'Last School Year', transform=ax.transAxes, fontsize=10)
    ax.text(0.12, 1.06, ' ', transform=ax.transAxes, fontsize=1, bbox=dict(facecolor=GROWTH_GREEN, alpha=1))
    ax.text(0.7, 1.05, 'This School Year', transform=ax.transAxes, fontsize=10)
    ax.text(0.66, 1.06, ' ', transform=ax.transAxes, fontsize=1, bbox=dict(facecolor=DEEP_BLUE, alpha=1))
    

    # Set the labels and title
    ax.set_title('YEAR-OVER-YEAR • ' + "Sacks", fontsize=16, weight='bold',color = DEEP_BLUE,pad=25)
    
    ax.set_xlabel('')
    ax.set_ylabel('')
    
    ax.set_xticks(range(0,2,1))
    ax.set_xticks(ticks=[0.25, .75], labels=[calendar.month_name[monthNum - 1], calendar.month_name[monthNum]])


    max_play_count = int(max(play_counts) * 6/5)
    min_play_count = 0

    #print(play_counts)
    yspace = 0

    yspacevals = [2,5,10,20,50,100,200,500,1000]

    yspace = min(yspacevals, key=lambda y: abs(y - max(play_counts) / 6))


    ax.set_yticks(range(min_play_count,max_play_count,yspace))#make variable based on data range

    ax.set_facecolor(WHITE)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)

    return ax


    