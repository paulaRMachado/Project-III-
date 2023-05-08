import pandas as pd

def basic_clean(df):
    """
    This function removes duplicates and NaNs from any given dataframe
    arg:
    :df: a dataframe to be cleaned
    returns:
    :clean_df: 
    """
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    return df
