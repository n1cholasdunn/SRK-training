def get_gym_training(sheet_fetcher):
    data = sheet_fetcher.fetch_data(sheet_index=1, start_cell="B27", end_cell="L37")
    return data


def get_otw_training(sheet_fetcher):
    data = sheet_fetcher.fetch_training_data(
        sheet_index=1, start_cell="B11", end_cell="L25"
    )
    return data


def get_prehab_training(sheet_fetcher):
    data = sheet_fetcher.fetch_data(sheet_index=1, start_cell="B40", end_cell="L42")
    return data
