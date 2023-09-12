from backend.gspread.utils.gsheet_fetcher import fetcher


def get_sharks_skills():
    data = fetcher.fetch_data(sheet_index=3, start_cell="A60", end_cell="L73")
    return data


print(get_sharks_skills)
