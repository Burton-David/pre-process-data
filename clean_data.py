def clean_data(df):
    """
    Cleans a Pandas dataframe by performing the following steps:
     - Removes rows with missing values
     - Drops duplicate rows
     - Replaces invalid or out-of-range values with NaN
     - Imputes missing values using the median or mode
     - Normalizes numerical columns

    Parameters:
    df (pandas.DataFrame): The dataframe to clean.

    Returns:
    pandas.DataFrame: The cleaned dataframe.
    """
    # Remove rows with missing values
    df.dropna(inplace=True)

    # Drop duplicate rows
    df.drop_duplicates(inplace=True)

    # Replace invalid or out-of-range values with NaN
    df.replace([-9999, 9999], pd.np.nan, inplace=True)

    # Impute missing values using the median or mode
    for col in df.columns:
        if df[col].dtype == 'float64':
            df[col].fillna(df[col].median(), inplace=True)
        elif df[col].dtype == 'object':
            df[col].fillna(df[col].mode()[0], inplace=True)

    # Normalize numerical columns
    df = (df - df.mean()) / df.std()

    return df
