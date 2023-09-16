from gsheets.utils.fetchAndFormat.gsheet_fetcher import fetcher

# TODO custom fetch function for formatting this properly


def get_program_info():
    data = fetcher.fetch_program_data(sheet_index=0, start_cell="A11", end_cell="H17")
    return data


print(get_program_info())
