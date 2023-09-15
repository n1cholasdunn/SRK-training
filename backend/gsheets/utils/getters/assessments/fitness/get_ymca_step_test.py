from gsheets.utils.fetchAndFormat.gsheet_fetcher import fetcher


def get_ymca_step_test():
    data = fetcher.fetch_data(sheet_index=3, start_cell="A43", end_cell="N44")
    return data
