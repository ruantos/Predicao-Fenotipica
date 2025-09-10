import pandas as pd
from extract import fetch_sheets

COLS_TO_DROP = {
	'main':
	[
		'Nome completo do voluntário: ', 'Idade na admissão: ',
		'Reside em qual cidade: ', 'Grau de instrução: ',
		'  Estado civil:   ', '  Profissão:  '
	],
	'genotypes':
	[
		'Nome completo do voluntário: ', 'Cor da pele: ',
		'  Cor dos olhos:  ', '  Cor dos cabelos quando tinha 15 anos:  ',
		'Número de identificação (Iniciar com EC, acrescido de três dígitos - ex: EC001): '
	]
}


def drop_columns(df: pd.DataFrame, sheet: int = 1) -> pd.DataFrame:
	if sheet == 1:
		return df.drop(columns=COLS_TO_DROP['main'])

	return df.drop(columns=COLS_TO_DROP['genotypes'])


def join_dataframes(df_1: pd.DataFrame, df_2: pd.DataFrame) -> pd.DataFrame:
	return df_1.join(df_2, how='outer')



if __name__ == '__main__':
	df_1, df_2 = fetch_sheets()
	df_1 = drop_columns(df_1, 1)
	df_2 = drop_columns(df_2, 2)

	df_combined = join_dataframes(df_1, df_2)
	print(df_combined.columns)