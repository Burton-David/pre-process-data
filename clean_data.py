import pandas as pd


def clean_data(df, remove_missing=True, drop_duplicates=True, replace_invalid=True, impute_missing=True, normalize=True):
    """
    Cleans a Pandas dataframe by performing the following steps:
     - Removes rows with missing values (optional)
     - Drops duplicate rows (optional)
     - Replaces invalid or out-of-range values with NaN (optional)
     - Imputes missing values using the mean, median, or mode (optional)
     - Normalizes numerical columns (optional)

    Parameters:
    df (pandas.DataFrame): The dataframe to clean.
    remove_missing (bool): Whether to remove rows with missing values.
    drop_duplicates (bool): Whether to drop duplicate rows.
    replace_invalid (bool): Whether to replace invalid or out-of-range values with NaN.
    impute_missing (bool): Whether to impute missing values.
    normalize (bool): Whether to normalize numerical columns.

    Returns:
    pandas.DataFrame: The cleaned dataframe.
    """
    if remove_missing:
        # Remove rows with missing values
        df.dropna(inplace=True)

    if drop_duplicates:
        # Drop duplicate rows
        df.drop_duplicates(inplace=True)

    if replace_invalid:
        # Replace invalid or out-of-range values with NaN
        df.replace([-9999, 9999], pd.np.nan, inplace=True
                   import pandas as pd

                   def clean_data(df, columns=None, remove_missing=True, drop_duplicates=True, replace_invalid=True, impute_missing=True, normalize=True):
                   """
    Cleans a Pandas dataframe by performing the following steps on specified columns:
     - Removes rows with missing values (optional)
     - Drops duplicate rows (optional)
     - Replaces invalid or out-of-range values with NaN (optional)
     - Imputes missing values using the mean, median, or mode (optional)
     - Normalizes numerical columns (optional)

    Parameters:
    df (pandas.DataFrame): The dataframe to clean.
    columns (list): The columns of the dataframe to perform the cleaning operations on.
    remove_missing (bool): Whether to remove rows with missing values.
    drop_duplicates (bool): Whether to drop duplicate rows.
    replace_invalid (bool): Whether to replace invalid or out-of-range values with NaN.
    impute_missing (bool): Whether to impute missing values.
    normalize (bool): Whether to normalize numerical columns.

    Returns:
    pandas.DataFrame: The cleaned dataframe.
    """
                   if columns is None:
                   columns=df.columns

                   if remove_missing:
                   # Remove rows with missing values
                   df.dropna(subset=columns, inplace=True)

                   if drop_duplicates:
                   # Drop duplicate rows
                   df.drop_duplicates(subset=columns, inplace=True)

                   if replace_invalid:
                   # Replace invalid or out-of-range values with NaN
                   df[columns].replace([-9999, 9999], pd.np.nan, inplace=True)
                   df[columns].replace(['N/A', 'NA', 'NULL', '?'],
                                       pd.np.nan, inplace=True)

                   if impute_missing:
                   # Impute missing values using the mean, median, or mode
                   for col in columns:
                   if df[col].dtype == 'float64':
