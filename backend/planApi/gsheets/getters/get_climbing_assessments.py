from planApi.gsheets.utils.gsheet_fetcher import fetcher


def get_power_endurance():
    data = fetcher.fetch_data(sheet_index=2, start_cell="A7", end_cell="L8")
    return data


def get_oa_pinch_finger_strength():
    data = fetcher.fetch_data(sheet_index=2, start_cell="B25", end_cell="L26")
    return data


def get_oa_finger_strength():
    data = fetcher.fetch_data(sheet_index=2, start_cell="B19", end_cell="L21")
    return data


def get_max_pullups():
    data = fetcher.fetch_data(sheet_index=2, start_cell="A30", end_cell="31")
    return data


def get_max_lockoff():
    data = fetcher.fetch_data(sheet_index=2, start_cell="A35", end_cell="L36")
    return data


def get_finger_strength():
    data = fetcher.fetch_data(sheet_index=2, start_cell="B13", end_cell="L15")
    return data
