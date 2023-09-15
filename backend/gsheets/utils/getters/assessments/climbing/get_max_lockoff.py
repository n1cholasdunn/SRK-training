from gsheets.utils.fetchAndFormat.gsheet_fetcher import fetcher


def get_max_lockoff():
    data = fetcher.fetch_data(sheet_index=2, start_cell="A35", end_cell="L36")
    return data
