from gsheets.utils.fetchAndFormat.gsheet_fetcher import fetcher


def get_oa_pinch_finger_strength():
    data = fetcher.fetch_data(sheet_index=2, start_cell="B25", end_cell="L26")
    return data
