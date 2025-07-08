import pandas as pd

def load_ehr_data(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print("Error loading file:", e)
        return None
