from backend.gspread.utils.gsheet_fetcher import fetcher


def get_pushups():
    data = fetcher.fetch_data(sheet_index=3, start_cell="B48", end_cell="O51")
    return data
