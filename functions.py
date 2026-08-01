import pandas as pd


# Function 1: Check duplicates in both datasets and removing them if there is any.
def check_duplicates (df, name ="dataset"):
    dup_count = df.duplicated().sum()
    print(f"{name} has duplicate rows: {dup_count}")
    return df.drop_duplicates().reset_index(drop=True)
    


# Function 2 : For dataset2: global_smartphone_addiction dataset 
# Changing Anxiety_Level and Depression_Level values - Scaling down to 1-10 range from 1-100
def scale_to_ten (df, column_name, threshold=10):
    """
    Scales a column down to a 0-10 range by dividing by 10,
    only if it hasn't already been scaled (safe to re-run).
    """
    if df[column_name].max() > threshold:
        df[column_name] = (df[column_name] / 10).round(1)
    return df


#Function 3: Combining dataset 1 and 2
# Check that both dataframes have the same columns
def combined_datasets(df1, df2):
    """
    This function combines two dataframes by keeping only their shared columns.
    Also checks for duplicate User_ID values after combining.
    """
    common_columns = list(set(df1.columns) & set(df2.columns))
    
    concat_df = pd.concat([df1[common_columns], df2[common_columns]], ignore_index=True)
    
    duplicate_ids = concat_df['User_ID'].duplicated().sum()
    if duplicate_ids > 0:
        print(f"Warning: {duplicate_ids} duplicate User_ID values found after concatenation.")
    else:
        print("Concatenated successful — no duplicate User_ID values.")
    
    return concat_df