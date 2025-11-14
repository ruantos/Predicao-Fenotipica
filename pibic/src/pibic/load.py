from supabase import create_client


def connect(project_url: str, api_key: str):
	try:
		client = create_client(project_url, api_key)
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
			print(f"{len(records)} records inserted successfully")
		else:
			print('Records list is empty')
	except Exception as e:
		print(f"Error caught while trying to insert records: {e}")


if __name__ == "__main__":
	pass



