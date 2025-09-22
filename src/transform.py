import pandas as pd


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


def rename_columns(df: pd.DataFrame) -> pd.DataFrame:
	return df.rename(columns={
		'Número de identificação (Iniciar com EC, acrescido de três dígitos - ex: EC001): ': 'id_voluntario',
		'Sexo (gênero):' : 'sexo',
		'Data de nascimento: ': 'data_nascimento',
		'Cor da pele: ': 'cor_pele',
		'Tipo de Pele (Classificação de Fitzpatrick):  ': 'tipo_pele',
		'  Cor dos olhos:  ': 'cor_olhos',
		'  Cor dos cabelos quando tinha 15 anos:  ': 'cor_cabelo_15_anos'
	})


def transform(df_1: pd.DataFrame, df_2: pd.DataFrame) -> pd.DataFrame:
	df_1 = drop_columns(df_1, 1)
	df_2 = drop_columns(df_2, 2)

	df = join_dataframes(df_1, df_2)
	df = rename_columns(df)


	return df