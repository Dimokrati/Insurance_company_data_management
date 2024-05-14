import requests
import pandas as pd

class DataExtractor:
    def __init__(self):
        pass

    def extract_from_api(self, api_url):
        """
        Extract data from an API.

        Args:
            api_url (str): URL of the API endpoint.

        Returns:
            pandas.DataFrame: DataFrame containing the extracted data.
        """
        try:
            response = requests.get(api_url)
            response.raise_for_status()  # Raise an exception for HTTP errors
            data = response.json()
            # Check if data is a dictionary or a list
            if isinstance(data, list):
                # If data is a list, assume it contains only one element
                data = data[0]
            # Initialize an empty DataFrame
            dfs = list(map(lambda category: pd.json_normalize(data[category]).add_prefix(category+'_'), data))
            # Concatenate the flattened DataFrames
            df = pd.concat(dfs, axis=1)
            return df
        except requests.RequestException as e:
            print(f"Error extracting data from API: {e}")
            return None


