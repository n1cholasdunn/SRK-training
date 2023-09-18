from gsheets.utils.fetchAndFormat.gsheet_fetcher import fetcher


def get_otw_training():
    data = fetcher.fetch_training_data(sheet_index=1, start_cell="B11", end_cell="L25")
    return data


# print(get_otw_training())
