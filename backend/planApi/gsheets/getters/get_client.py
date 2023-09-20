from planApi.gsheets.utils.gsheet_fetcher import fetcher


def get_program_info():
    data = fetcher.fetch_program_data(sheet_index=0, start_cell="A11", end_cell="H17")
    return data


def get_equipment():
    data = fetcher.fetch_data(sheet_index=0, start_cell="A24", end_cell="J26")
    return data


def get_client_info():
    data = fetcher.fetch_client_data(sheet_index=0, start_cell="A2", end_cell="J9")
    return data


def get_availability():
    data = fetcher.fetch_client_availability(
        sheet_index=0, start_cell="A19", end_cell="H21"
    )
    return data
