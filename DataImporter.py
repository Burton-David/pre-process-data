class DataImporter:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def import_data(self, file_type: str) -> pd.DataFrame:
        """Import data from a file and return it as a Pandas DataFrame.

        Args:
        - file_type: The type of file to be imported (e.g. 'csv', 'excel', 'json').

        Returns:
        - A Pandas DataFrame containing the data from the file.
        """
        if file_type == 'csv':
            return pd.read_csv(self.file_path)
        elif file_type == 'excel':
            return pd.read_excel(self.file_path)
        elif file_type == 'json':
            return pd.read_json(self.file_path)
        else:
            raise ValueError(f'Unsupported file type: {file_type}')
