from planApi.gsheets.utils.gsheet_fetcher import GoogleSheetsFetcher


def fetch_url_data(url, func):
    sheets_fetcher = GoogleSheetsFetcher(url)
    return func(sheets_fetcher)
