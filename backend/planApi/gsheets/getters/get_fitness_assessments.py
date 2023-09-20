from planApi.gsheets.utils.gsheet_fetcher import fetcher


def get_ymca_step_test():
    data = fetcher.fetch_data(sheet_index=3, start_cell="A43", end_cell="N44")
    return data


def get_sit_reach():
    data = fetcher.fetch_data(sheet_index=3, start_cell="D22", end_cell="O26")
    return data


def get_sharks_skills():
    data = fetcher.fetch_data(sheet_index=3, start_cell="A60", end_cell="L73")
    return data


def get_pushups():
    data = fetcher.fetch_data(sheet_index=3, start_cell="B48", end_cell="O51")
    return data


def get_overhead_squat():
    data = fetcher.fetch_data(sheet_index=3, start_cell="D22", end_cell="O26")
    return data


def get_davies():
    data = fetcher.fetch_data(sheet_index=3, start_cell="B54", end_cell="O57")
    return data


def get_core_strength():
    data = fetcher.fetch_data(sheet_index=3, start_cell="B76", end_cell="O78")
    return data
