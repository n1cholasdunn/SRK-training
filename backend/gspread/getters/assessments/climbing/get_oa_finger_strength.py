from backend.gspread.utils.gsheet_fetcher import fetcher


def get_oa_finger_strength():
    data = fetcher.fetch_data(sheet_index=2, start_cell="B19", end_cell="L21")
    return data
