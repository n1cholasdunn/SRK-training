from backend.gspread.utils.gsheet_fetcher import fetcher


def get_pt_prehab():
    data = fetcher.fetch_data(sheet_index=1, start_cell="B11", end_cell="L25")
    return data
