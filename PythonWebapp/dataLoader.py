import pandas as pd
import os

DATA_FOLDER = os.path.join(os.getcwd(), "data")
CSV_FILE_PATH = os.path.join(DATA_FOLDER, "testdata.csv")

GRAPH_FOLDER = os.path.join(os.getcwd(), "graphs")

def get_dropdown_options():
    df = pd.read_csv(CSV_FILE_PATH)
    return df['classrooms_text'].unique()

def get_files_in_folder(folder_path):
    # Get a list of all file names in the folder
    files = [os.path.splitext(f)[0] for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    return files
