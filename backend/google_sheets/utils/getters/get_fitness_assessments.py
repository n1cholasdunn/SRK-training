def get_health_markers(sheet_fetcher):
    data = sheet_fetcher.fetch_data(sheet_index=3, start_cell="B4", end_cell="N9")
    return data


def get_measurements(sheet_fetcher):
    data = sheet_fetcher.fetch_data(sheet_index=3, start_cell="B12", end_cell="N19")
    return data


def get_ymca_step_test(sheet_fetcher):
    data = sheet_fetcher.fetch_data(sheet_index=3, start_cell="B33", end_cell="O35")
    return data


def get_sit_reach(sheet_fetcher):
    data = sheet_fetcher.fetch_data(sheet_index=3, start_cell="A44", end_cell="N46")
    return data


def get_sharks_skills(sheet_fetcher):
    data = sheet_fetcher.fetch_shark_skills_data(
        sheet_index=3, start_cell="A60", end_cell="L73"
    )
    return data


def get_pushups(sheet_fetcher):
    data = sheet_fetcher.fetch_data(sheet_index=3, start_cell="B48", end_cell="O51")
    return data


def get_overhead_squat(sheet_fetcher):
    data = sheet_fetcher.fetch_data(sheet_index=3, start_cell="D23", end_cell="O29")
    return data


def get_davies(sheet_fetcher):
    data = sheet_fetcher.fetch_data(sheet_index=3, start_cell="B55", end_cell="O57")
    return data


def get_core(sheet_fetcher):
    data = sheet_fetcher.fetch_data(sheet_index=3, start_cell="B77", end_cell="O78")
    return data
