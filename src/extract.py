import pandas as pd
import dotenv
import os
import gspread

dotenv.load_dotenv()

id_list = {
	'spreadsheet_id': os.environ.get("SPREADSHEET_ID"),
	'sheet_id_main': os.environ.get("SHEET_ID_GERAL"),
	'sheet_id_genotypes': os.environ.get("SHEET_ID_GENOTIPOS")
}


def fetch_sheets(ids: dict[str, str]) -> tuple[pd.DataFrame, pd.DataFrame] | None:

	try:
		google_client = gspread.service_account(filename='../.auth.json')
		spreadsheet = google_client.open_by_key(ids['spreadsheet_id'])

		data_genotypes = (spreadsheet
		                  .get_worksheet_by_id(ids['sheet_id_genotypes'])
		                  .get_all_records())
		data_main = (spreadsheet
		             .get_worksheet_by_id(ids['sheet_id_main'])
		             .get_all_records())

		return pd.DataFrame(data_main),  pd.DataFrame(data_genotypes, )

	except Exception as e:
		print(f'Error caught while fetching sheets: {e}')
		return None
