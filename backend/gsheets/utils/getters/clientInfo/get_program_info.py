from gsheets.utils.fetchAndFormat.gsheet_fetcher import fetcher


def get_program_info():
    data = fetcher.fetch_data(sheet_index=0, start_cell="A11", end_cell="H16")
    return data
