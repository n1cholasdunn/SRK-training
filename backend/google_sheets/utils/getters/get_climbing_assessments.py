def get_power_endurance(sheet_fetcher):
    data = sheet_fetcher.fetch_test_with_seconds(
        sheet_index=2, start_cell="A7", end_cell="L8"
    )
    return data


def get_oa_pinch_finger_strength(sheet_fetcher):
    data = sheet_fetcher.fetch_pinch_strength(
        sheet_index=2, start_cell="B25", end_cell="L26"
    )
    return data


def get_oa_finger_strength(sheet_fetcher):
    data = sheet_fetcher.fetch_oa_finger_strength(
        sheet_index=2, start_cell="B19", end_cell="L21"
    )
    return data


def get_max_pullups(sheet_fetcher):
    data = sheet_fetcher.fetch_test_with_seconds(
        sheet_index=2, start_cell="A30", end_cell="31"
    )
    return data


def get_max_lockoff(sheet_fetcher):
    data = sheet_fetcher.fetch_test_with_seconds(
        sheet_index=2, start_cell="A35", end_cell="L36"
    )
    return data


def get_finger_strength(sheet_fetcher):
    data = sheet_fetcher.fetch_finger_strength(
        sheet_index=2, start_cell="B13", end_cell="L15"
    )
    return data
