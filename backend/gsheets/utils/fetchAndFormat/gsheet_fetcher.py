import gspread
from .remove_whitespace import remove_empty_elements
from .creds import credentials


class GoogleSheetsFetcher:
    """Class to fetch & format sheet data"""

    def __init__(self, sheet_url):
        self.gc = gspread.service_account_from_dict(credentials)
        self.sh = self.gc.open_by_url(sheet_url)

    def fetch_data(self, sheet_index, start_cell, end_cell):
        try:
            worksheet = self.sh.get_worksheet(sheet_index)
            data = worksheet.get(f"{start_cell}:{end_cell}")
            filtered_data = remove_empty_elements(data)
            return filtered_data
        except Exception as e:
            print(f"Error fetching data: {e}")
            return []

    def fetch_raw_data(self, sheet_index, start_cell, end_cell):
        try:
            worksheet = self.sh.get_worksheet(sheet_index)
            data = worksheet.get(f"{start_cell}:{end_cell}")
            return data
        except Exception as e:
            print(f"Error fetching data: {e}")
            return []


# Example usage
sheet = "https://docs.google.com/spreadsheets/d/16eR5pzMGubEou4c5-JBm86zoqbrco71ZlGrX-HZG6ig/edit?usp=sharing"
fetcher = GoogleSheetsFetcher(sheet)

# Fetch data from sheet index 1, cells B11 to L25
data = fetcher.fetch_data(sheet_index=1, start_cell="B11", end_cell="L25")

print(data)
