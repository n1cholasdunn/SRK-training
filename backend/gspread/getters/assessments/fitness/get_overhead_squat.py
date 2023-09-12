from backend.gspread.utils.gsheet_fetcher import fetcher


def get_overhead_squat():
    data = fetcher.fetch_data(sheet_index=3, start_cell="D22", end_cell="O26")
    return data
