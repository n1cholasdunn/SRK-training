from gsheets.utils.fetchAndFormat.gsheet_fetcher import fetcher


def get_availability():
    data = fetcher.fetch_data(sheet_index=0, start_cell="A19", end_cell="H21")
    return data
