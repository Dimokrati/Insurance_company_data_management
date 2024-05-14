from etl.extract.fetch_api import DataExtractor
import pandas as pd
data_extractor = DataExtractor()

# Extract data from API
api_url = 'https://my.api.mockaroo.com/policy_sales.json?key=07cac880'
data = data_extractor.extract_from_api(api_url)

print(data)