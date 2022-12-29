import requests
import pandas as pd


class APIImporter:
    def __init__(self, api_url: str):
        self.api_url = api_url

    def get_data(self, endpoint: str, params: dict = None) -> pd.DataFrame:
        """Retrieve data from the API and return it as a Pandas DataFrame.

        Args:
        - endpoint: The API endpoint to send the request to.
        - params: A dictionary of query parameters to include in the request.

        Returns:
        - A Pandas DataFrame containing the data from the API.
        """
        url = f'{self.api_url}/{endpoint}'
        response = requests.get(url, params=params)
        data = response.json()
        return pd.DataFrame(data)

    def get_data_by_page(self, endpoint: str, page_size: int, params: dict = None) -> pd.DataFrame:
        """Retrieve data from the API in chunks, using pagination.

        Args:
        - endpoint: The API endpoint to send the request to.
        - page_size: The number of records to include in each page of data.
        - params: A dictionary of query parameters to include in the request.

        Returns:
        - A Pandas DataFrame containing the data from the API.
        """
        df = pd.DataFrame()
        page = 1
        while True:
            params['page'] = page
            page_data = self.get_data(endpoint, params=params)
            if page_data.empty:
                break
            df = df.append(page_data)
            page += 1
        return df

    def get_data_by_date_range(self, endpoint: str, start_date: str, end_date: str, params: dict = None) -> pd.DataFrame:
        """Retrieve data from the API for a specific date range.

        Args:
        - endpoint: The API endpoint to send the request to.
        - start_date: The start date for the date range (in the format 'YYYY-MM-DD').
        - end_date: The end date for the date range (in the format 'YYYY-MM-DD').
        - params: A dictionary of query parameters to include in the request.

        Returns:
        - A Pandas DataFrame containing the data from the API.
        """
        params['start_date'] = start_date
        params['end_date'] = end_date
        return self.get_data(endpoint, params=params)

    def get_data_by_location(self, endpoint: str, latitude: float, longitude: float, radius: float, params: dict = None) -> pd.DataFrame:
        """Retrieve data from the API for a specific geographic location.

        Args:
        - endpoint: The API endpoint to send the request to.
        - latitude: The latitude of the location.
        - longitude: The longitude of the location.
        - radius: The radius around the location to include data for, in kilometers.
        - params: A dictionary of query parameters to include in the request.

        Returns:
        - A Pandas DataFrame containing the data from the API.
        """
        params['latitude'] = latitude
        params['longitude'] = longitude
        params['radius'] = radius
        return self.get_data(endpoint, params=params)

    def get_data_by_id(self, endpoint: str, id: int, params: dict = None) -> pd.DataFrame:
        """Retrieve data from the API for a specific record, identified by its ID.

        Args:
        - endpoint: The API endpoint to send the request to.
        - id: The ID of the record to retrieve.
        - params: A dictionary of query parameters to include in the request.

        Returns:
        - A Pandas DataFrame containing the data from the API.
        """
        endpoint = f'{endpoint}/{id}'
        return self.get_data(endpoint, params=params)

    def get_data_by_query(self, endpoint: str, query: str, params: dict = None) -> pd.DataFrame:
        """Retrieve data from the API using a search query.

        Args:
        - endpoint: The API endpoint to send the request to.
        - query: The search query to use.
        - params: A dictionary of query parameters to include in the request.

        Returns:
        - A Pandas DataFrame containing the data from the API.
        """
        params['q'] = query
        return self.get_data(endpoint, params=params)
