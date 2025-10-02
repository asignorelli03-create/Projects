import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import calendar
from dateutil.relativedelta import relativedelta
from styles.Colors import (GROWTH_GREEN, DEEP_BLUE, WHITE, FFL_BLACK, EXPLORE_YELLOW, BRONZE, INSPIRE_RED, LIGHT_GRAY, DARK_GRAY)
import os

def createGraph(ax, month=None, year=None, classroom=None):
    # Load the dataset
    GRAPH_FOLDER = os.path.join(os.getcwd(), "data")
    CSV_FILE_PATH = os.path.join(GRAPH_FOLDER, "testdata.csv")

    # Read the CSV file
    df = pd.read_csv(CSV_FILE_PATH)

    # Convert 'dateTime' to pandas datetime format
    df['dateTime'] = pd.to_datetime(df['dateTime'])

    # Filter rows where 'type' is 'First Down'
    firstdown_df = df[df['type'] == 'Sack']

    # Ensure proper datetime format without timezone
    firstdown_df.loc[:, 'dateTime'] = pd.to_datetime(firstdown_df['dateTime'], errors='coerce')

    # Convert datetime to period, remove timezone if needed
    firstdown_df.loc[:, 'MonthYear'] = firstdown_df['dateTime'].dt.tz_localize(None).dt.to_period("M")
    
    # Filter by month and year if provided
    if month is not None and year is not None:
        # Convert month and year to integers if they're strings
        month_int = int(month) if isinstance(month, str) else month
        year_int = int(year) if isinstance(year, str) else year
        
        # Create a datetime for the selected month/year
        target_date = pd.Timestamp(year=year_int, month=month_int, day=1)
        
        # Calculate 3 months before and 3 months after
        start_date = target_date - relativedelta(months=3)
        end_date = target_date
        
        # Convert to periods for filtering
        start_period = pd.Period(start_date, freq='M')
        end_period = pd.Period(end_date, freq='M')
        
        # Filter data for the range of months
        firstdown_df = firstdown_df[(firstdown_df['MonthYear'] >= start_period) & 
                                   (firstdown_df['MonthYear'] <= end_period)]
        
        # Add classroom filter if provided
        if classroom is not None and 'classroom' in firstdown_df.columns:
            firstdown_df = firstdown_df[firstdown_df['classroom'] == classroom]

    # After plotting
    ax.figure.subplots_adjust(hspace=0.5, wspace=0.3)  # Adjust horizontal and vertical spacing

    # Count occurrences per month
    monthly_counts = firstdown_df['MonthYear'].value_counts().sort_index()

    # Create DataFrame for plotting
    df2 = pd.DataFrame({
        "Month": monthly_counts.index.astype(str),
        "Count": monthly_counts.values
    })

    # Plotting using Seaborn
    sns.lineplot(
        ax=ax,  # Pass the specific axes object
        x="Month",
        y="Count",
        data=df2,
        marker="o",
        color=DEEP_BLUE,  # Line color
        markeredgecolor=FFL_BLACK,
        linewidth=2.5
    )

    # Customize the grid
    ax.grid(True, linestyle='--', alpha=0.5)
    
    # Set labels and title
    title = 'Monthly Sacks'
    
    ax.set_title(
        title,
        fontsize=16,
        color=DEEP_BLUE,
        weight='bold',
        pad=20
    )
    ax.set_xlabel('Month', fontsize=12)
    ax.set_ylabel('Count', fontsize=12)

    # Set background color
    ax.set_facecolor(WHITE)

    # Customize spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_color(DARK_GRAY)

    # Rotate x-axis labels for better readability
    plt.setp(ax.get_xticklabels(), rotation=45, ha='right')

    return ax