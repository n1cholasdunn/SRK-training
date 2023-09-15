from gsheets.utils.fetchAndFormat.gsheet_fetcher import fetcher


def get_davies():
    data = fetcher.fetch_data(sheet_index=3, start_cell="B54", end_cell="O57")
    return data
