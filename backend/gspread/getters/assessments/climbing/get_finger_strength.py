from backend.gspread.utils.gsheet_fetcher import fetcher


def get_finger_strength():
    data = fetcher.fetch_data(sheet_index=2, start_cell="B13", end_cell="L15")
    return data
