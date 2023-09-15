from gsheets.utils.fetchAndFormat.gsheet_fetcher import fetcher


def get_equipment():
    data = fetcher.fetch_data(sheet_index=0, start_cell="A24", end_cell="J26")
    return data
