import pandas as pd


def load_csv(file_name):
    # Try to load the CSV file with the default arguments
    try:
        df = pd.read_csv(file_name)
        return df
    except:
        pass

    # Try to load the CSV file with a different delimiter
    try:
        df = pd.read_csv(file_name, sep='\t')
        return df
    except:
        pass

    # Try to load the CSV file with no header row
    try:
        df = pd.read_csv(file_name, header=None)
        return df
    except:
        pass

    # Try to load the CSV file with a different encoding
    try:
        df = pd.read_csv(file_name, encoding='latin1')
        return df
    except:
        pass

    # Try to load the CSV file with a different quoting style
    try:
        df = pd.read_csv(file_name, quoting=3)
        return df
    except:
        pass

    # If all attempts fail, raise an error
    raise ValueError('Unable to load CSV file')


if __name__ == '__main__':
    file_name = input('Enter the name of the CSV file: ')
    df = load_csv(file_name)
    print(df)
