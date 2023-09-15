from gsheets.utils.fetchAndFormat.gsheet_fetcher import fetcher


def get_max_pullups():
    data = fetcher.fetch_data(sheet_index=2, start_cell="A30", end_cell="31")
    return data
