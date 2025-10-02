import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from styles.Colors import (GROWTH_GREEN, DEEP_BLUE, WHITE, FFL_BLACK, EXPLORE_YELLOW, BRONZE, INSPIRE_RED, LIGHT_GRAY, DARK_GRAY)
import os
# Set Seaborn global theme
sns.set_theme(style="whitegrid")

def createGraph(ax,monthNum,yearNum):
    # Load the CSV file
    GRAPH_FOLDER = os.path.join(os.getcwd(), "data")
    CSV_FILE_PATH = os.path.join(GRAPH_FOLDER, "checkintest.csv")
    df = pd.read_csv(CSV_FILE_PATH)


    if 'dateTime' in df.columns:
        df['dateTime'] = pd.to_datetime(df['dateTime'])
        # Filter by month and year
        df = df[(df['dateTime'].dt.month == monthNum) & (df['dateTime'].dt.year == yearNum)]

    # Count occurrences of each value (1-10) in the 'stress' column
    counts = df['stress'].value_counts().reindex(range(1, 11), fill_value=0)

    # Convert counts to a DataFrame for plotting
    df_counts = pd.DataFrame({
        'Value': counts.index,
        'Count': counts.values
    })

    # Set background color
    ax.set_facecolor(WHITE)
    ax.figure.set_facecolor(WHITE)

    # Plot the bar chart with white bars and specified text colors
    sns.barplot(x='Value', y='Count', data=df_counts, color=DEEP_BLUE, ax=ax)

    # Customize the plot
    ax.set_title('Check-In Levels', fontsize=16, fontweight='bold', color=DEEP_BLUE)
    ax.set_xlabel('')  # Remove the x-axis label
    ax.set_ylabel('Count', fontweight='bold', color=DEEP_BLUE)
    ax.tick_params(axis='x', labelsize=12, labelcolor=DEEP_BLUE)  # Set x-tick labels size and color
    ax.tick_params(axis='y', labelcolor=DEEP_BLUE)  # Set y-tick labels color

    # Define label height for easy adjustment
    label_height = -350

    # Add "Low", "Moderate", and "High" labels at the defined label height
    ax.text(1, label_height, "Low", fontsize=12, color=DEEP_BLUE, ha="center", fontweight='bold')
    ax.text(5, label_height, "Moderate", fontsize=12, color=DEEP_BLUE, ha="center", fontweight='bold')
    ax.text(8, label_height, "High", fontsize=12, color=DEEP_BLUE, ha="center", fontweight='bold')

    # Adjust plot limits to make space for new labels
    ax.set_ylim(df_counts['Count'].min() - 10, df_counts['Count'].max() + 5)

    # Adjust layout manually instead of using tight_layout()
    #ax.subplots_adjust(bottom=0.2)

    return ax

# Uncomment to generate the plot
# fig, ax = plt.subplots()
# generate_check_in_levels(ax)
# plt.show()
