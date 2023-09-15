from gsheets.utils.fetchAndFormat.gsheet_fetcher import fetcher


def get_core_strength():
    data = fetcher.fetch_data(sheet_index=3, start_cell="B76", end_cell="O78")
    return data
