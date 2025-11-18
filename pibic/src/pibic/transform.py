import numpy as np
import pandas as pd


COLS_TO_DROP = {
	'main':
		[
		'Nome completo do voluntário: ', 'Idade na admissão: ',
		'Reside em qual cidade: ', 'Grau de instrução: ',
		'  Estado civil:   ', '  Profissão:  ', 'Sexo (gênero):',
		'Data de nascimento: ', 'Tipo de Pele (Classificação de Fitzpatrick):  '
		],
	'genotypes':
		[
		'Nome completo do voluntário: ', 'Cor da pele: ',
		'  Cor dos olhos:  ', '  Cor dos cabelos quando tinha 15 anos:  ',
		'Número de identificação (Iniciar com EC, acrescido de três dígitos - ex: EC001): '
		],
	'juliana':
		[
		'Nome completo do voluntário: '
		]
}


def drop_columns(df: pd.DataFrame, sheet: int = 1) -> pd.DataFrame:
	if sheet == 1:
		return df.drop(columns=COLS_TO_DROP['main'])
	if sheet == 2:
		return df.drop(columns=COLS_TO_DROP['genotypes'])
	return df.drop(columns=COLS_TO_DROP['juliana'])


def join_dataframes(df_1: pd.DataFrame, df_2: pd.DataFrame) -> pd.DataFrame:
	return df_1.join(df_2, how='outer')


def rename_columns(df: pd.DataFrame) -> pd.DataFrame:
	return df.rename(columns={
		'Número de identificação (Iniciar com EC, acrescido de três dígitos - ex: EC001): ': 'id_voluntario',
		'Data de nascimento: ': 'data_nascimento',
		'Cor da pele: ': 'cor_pele',
		'  Cor dos olhos:  ': 'cor_olhos',
		'  Cor dos cabelos quando tinha 15 anos:  ': 'cor_cabelo_15_anos'
	})

def concatenate_dfs(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
	return pd.concat([df1, df2], ignore_index=True)


def capitalize_columns(df: pd.DataFrame) -> pd.DataFrame:
	df['cor_pele'] = df['cor_pele'].str.capitalize()
	df['cor_olhos'] = df['cor_olhos'].str.capitalize()
	df['cor_cabelo_15_anos'] = df['cor_cabelo_15_anos'].str.capitalize()
	return df


def standardize_skin_color(df: pd.DataFrame) -> pd.DataFrame:
	df['cor_pele'] = (df['cor_pele'].replace('Moreno', 'Morena')
	 .replace('Preto', 'Preta')
	 .replace('Negro', 'Preta')
	 .replace('Branco', 'Branca'))

	return df


def standardize_hair_color(df: pd.DataFrame) -> pd.DataFrame:
	df['cor_cabelo_15_anos'] = (
		df['cor_cabelo_15_anos']
		.replace('Castanhos', 'Castanho')
		.replace('Loiros', 'Louro')
		.replace('Castanhos', 'Castanho')
		)
	return df


def standardize_eye_color(df: pd.DataFrame) -> pd.DataFrame:
	df['cor_olhos'] = (
		df['cor_olhos']
		.replace('Mel', 'Castanho')
		.replace('Castanho escuro', 'Castanho')
		.replace('Castanho claro', 'Castanho')
		)
	return df


def address_null_values(df: pd.DataFrame) -> pd.DataFrame:
	df['rs1426654'] = df['rs1426654'].replace('', np.nan)
	df['rs6058017'] = df['rs6058017'].replace('', np.nan)
	df['rs1800404'] = df['rs1800404'].replace('', np.nan)
	df['rs16891982'] = df['rs16891982'].replace('', np.nan)

	return df


def transform(dfs: list[pd.DataFrame]) -> pd.DataFrame:
	df_1 = drop_columns(dfs[0], 1)
	df_2 = drop_columns(dfs[1], 2)
	df_3 = drop_columns(dfs[2], 3)

	df = join_dataframes(df_1, df_2)
	df = concatenate_dfs(df, df_3)
	df = rename_columns(df)
	df = capitalize_columns(df)
	df = standardize_skin_color(df)
	df = standardize_hair_color(df)
	df = standardize_eye_color(df)
	df = address_null_values(df)


	return df