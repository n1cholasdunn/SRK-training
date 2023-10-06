import gspread
from .remove_whitespace import remove_empty_elements
from .creds import credentials
from .format_client_data import format_client_data
from .format_client_availability import format_availability
from .format_program_data import format_program_data
from .remove_whitespace_training import remove_otw_empty_elements
from .format_fitness import format_shark_skills_data


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

    def fetch_client_data(self, sheet_index, start_cell, end_cell):
        try:
            worksheet = self.sh.get_worksheet(sheet_index)
            data = worksheet.get(f"{start_cell}:{end_cell}")
            filtered_data = format_client_data(data)
            return filtered_data
        except Exception as e:
            print(f"Error fetching data: {e}")
            return []

    def fetch_client_availability(self, sheet_index, start_cell, end_cell):
        try:
            worksheet = self.sh.get_worksheet(sheet_index)
            data = worksheet.get(f"{start_cell}:{end_cell}")
            filtered_data = format_availability(data)
            return filtered_data
        except Exception as e:
            print(f"Error fetching data: {e}")
            return []

    def fetch_program_data(self, sheet_index, start_cell, end_cell):
        try:
            worksheet = self.sh.get_worksheet(sheet_index)
            data = worksheet.get(f"{start_cell}:{end_cell}")
            filtered_data = format_program_data(data)
            return filtered_data
        except Exception as e:
            print(f"Error fetching data: {e}")
            return []

    def fetch_training_data(self, sheet_index, start_cell, end_cell):
        try:
            worksheet = self.sh.get_worksheet(sheet_index)
            data = worksheet.get(f"{start_cell}:{end_cell}")
            filtered_data = remove_otw_empty_elements(data)
            return filtered_data
        except Exception as e:
            print(f"Error fetching data: {e}")
            return []

    def fetch_shark_skills_data(self, sheet_index, start_cell, end_cell):
        try:
            worksheet = self.sh.get_worksheet(sheet_index)
            data = worksheet.get(f"{start_cell}:{end_cell}")
            filtered_data = format_shark_skills_data(data)
            return filtered_data
        except Exception as e:
            print(f"Error fetching data: {e}")
            return []


# Example usage
sheet = "https://docs.google.com/spreadsheets/d/16eR5pzMGubEou4c5-JBm86zoqbrco71ZlGrX-HZG6ig/edit?usp=sharing"
fetcher = GoogleSheetsFetcher(sheet)

# # Fetch data from sheet index 1, cells B11 to L25
# data = fetcher.fetch_data(sheet_index=1, start_cell="B11", end_cell="L25")
