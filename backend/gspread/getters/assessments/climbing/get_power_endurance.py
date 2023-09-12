from backend.gspread.utils.gsheet_fetcher import fetcher


def get_power_endurance():
    data = fetcher.fetch_data(sheet_index=2, start_cell="A7", end_cell="L8")
    return data
