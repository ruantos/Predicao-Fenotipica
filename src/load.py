import supabase
import os
from dotenv import load_dotenv
from supabase import create_client


def connect(project_url: str, api_key: str):
	try:
		client = create_client(URL, KEY)
		print("Connection successful")
		return client

	except Exception as e:
		print(f"Error caught while trying to connect: {e}")
		return None


def insert_records(client, df):
	records = df.to_dict('records')

	try:
		if records:
			(
			client.table('individuos')
		    .insert(records)
		    .execute()
		    )
		else:
			print('Records list is empty')
	except Exception as e:
		print(f"Error caught while trying to insert records: {e}")


if __name__ == "__main__":
	load_dotenv()

	URL = os.getenv("SUPA_URL")
	KEY = os.getenv("SUPA_KEY")
	connect(URL, KEY)




