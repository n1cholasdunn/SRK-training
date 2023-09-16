from gsheets.utils.fetchAndFormat.gsheet_fetcher import fetcher

# TODO custom fetch function for formatting this properly


def get_client_info():
    data = fetcher.fetch_client_data(sheet_index=0, start_cell="A2", end_cell="J9")
    return data
