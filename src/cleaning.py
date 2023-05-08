import pandas as pd
import src.extraction as extract

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
# For the bonus
def transform(df):
    df["geo"] = df["address"].apply(extract.get_coordinates)
    return df

def deep_clean(df):
    df = df.drop(columns= ["Unnamed: 0","Unnamed: 0.1"])
    df['latitude'] = df['geo'].str.replace("'", "").str.extract('\((.*),.*\)', expand=True).astype(float)
    df['longitude'] = df['geo'].str.replace("'", "").str.extract('.*,\s*(.*)\)', expand=True).astype(float)

    # remove the original "geo" column
    df.drop('geo', axis=1, inplace=True)
    return df
