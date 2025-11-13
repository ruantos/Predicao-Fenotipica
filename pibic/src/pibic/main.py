from dotenv import load_dotenv
from extract import fetch_sheets
from transform import transform
from load import connect, insert_records
import os


if __name__ == '__main__':
	load_dotenv()

	id_list = {
		'spreadsheet_id': os.getenv("SPREADSHEET_ID"),
		'sheet_id_main': os.getenv("SHEET_ID_GERAL"),
		'sheet_id_genotypes': os.getenv("SHEET_ID_GENOTIPOS"),
		'sheet_id_juliana': os.getenv("SHEET_ID_JULIANA")
	}
	SUPA_URL = os.getenv("SUPA_URL")
	SUPA_KEY = os.getenv("SUPA_KEY")


	dfs  = fetch_sheets(id_list)
	df = transform(dfs)
	client = connect(SUPA_URL, SUPA_KEY)
	insert_records(client, df)
