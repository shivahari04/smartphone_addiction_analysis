# Function 1: Check duplicates in both datasets and removing them if there is any.


import pandas as pd

def check_duplicates (df, name ="dataset"):
    dup_count = df.duplicated().sum()
    print(f"{name} has duplicate rows: {dup_count}")
    return df.drop_duplicates().reset_index(drop=True)
    


# Function 2 : Changing Anxiety_Level and Depression_Level values - Scaling down to 1-10 range from 1-100
def scale_to_ten (df, column_name, threshold=10):
    """
    Scales a column down to a 0-10 range by dividing by 10,
    only if it hasn't already been scaled (safe to re-run).
    """
    if df[column_name].max() > threshold:
        df[column_name] = (df[column_name] / 10).round(1)
    return df
