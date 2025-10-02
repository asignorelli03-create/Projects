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

    # Define the target emotions
    emotions = ["Excited", "Happy", "Calm", "Worried", "Sad", "Angry"]

    # Count occurrences of each target emotion in the 'emotion' column
    emotion_counts = df['emotion'].value_counts().reindex(emotions, fill_value=0)

    # Convert counts to a DataFrame for plotting
    df_emotion_counts = pd.DataFrame({
        'Emotion': emotion_counts.index,
        'Count': emotion_counts.values
    })

    # Set background color
    ax.set_facecolor(WHITE)
    ax.figure.set_facecolor(WHITE)

    # Plot the bar chart with white bars
    sns.barplot(x='Emotion', y='Count', data=df_emotion_counts, color=DEEP_BLUE, ax=ax)

    # Customize the plot with specified text colors
    ax.set_title('Check-In Emotions', fontsize=16, fontweight='bold', color=DEEP_BLUE)
    ax.set_xlabel('Emotion', fontweight='bold', color=DEEP_BLUE)
    ax.set_ylabel('Count', fontweight='bold', color=DEEP_BLUE)
    ax.tick_params(axis='x', labelcolor=DEEP_BLUE)  # Set x-tick labels color
    ax.tick_params(axis='y', labelcolor=DEEP_BLUE)  # Set y-tick labels color

    # Adjust plot limits to make space for labels
    ax.set_ylim(df_emotion_counts['Count'].min() - 10, df_emotion_counts['Count'].max() + 5)

    # Adjust layout manually to prevent layout issues
    #ax.subplots_adjust(bottom=0.2)

    return ax

# Example usage:
# fig, ax = plt.subplots(figsize=(10, 6))
# generate_check_in_emotions(ax)
# plt.show()
