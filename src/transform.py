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

def reduce_col_sex(df: pd.DataFrame) -> pd.DataFrame:
	df['sexo'] = df['sexo'].str[0]
	return df


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

def transform(dfs: list[pd.DataFrame]) -> pd.DataFrame:
	df_1 = drop_columns(dfs[0], 1)
	df_2 = drop_columns(dfs[1], 2)
	df_3 = drop_columns(dfs[2], 3)

	df = join_dataframes(df_1, df_2)
	df = concatenate_dfs(df, df_3)
	df = rename_columns(df)
	df = reduce_col_sex(df)


	return df