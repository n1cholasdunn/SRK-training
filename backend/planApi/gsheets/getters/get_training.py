from planApi.gsheets.utils.gsheet_fetcher import fetcher


def get_gym_training():
    data = fetcher.fetch_data(sheet_index=1, start_cell="B27", end_cell="L37")
    return data


def get_otw_training():
    data = fetcher.fetch_training_data(sheet_index=1, start_cell="B11", end_cell="L25")
    return data


def get_prehab_training():
    data = fetcher.fetch_data(sheet_index=1, start_cell="B40", end_cell="L42")
    return data
