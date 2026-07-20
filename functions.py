# Function 1: Check duplicates in both datasets and removing them if there is any.


import pandas as pd

def check_duplicates (df, name ="dataset"):
    dup_count = df.duplicated().sum()
    print(f"{name} has duplicate rows: {dup_count}")
    return df.drop_duplicates().reset_index(drop=True)
    
