import pandas as pd
import kagglehub
import os
def rename_columns_snake_case(df):
    dataframe = df.copy()
    dataframe.columns = [col.lower().replace(" ", "_").replace("(", "_").replace(")", "")  for col in dataframe.columns]
    return dataframe

def data_reader(path: str):
    dataset_path = kagglehub.dataset_download(os.path.dirname(path))
    return pd.read_csv(os.path.join(dataset_path, os.path.basename(path)))

def check_column_names_and_missing_values(df):
    df_nulls = df.isnull().sum().reset_index()
    df_nulls.columns = ['col_name', 'num_nulls']
    return df_nulls

def nulls_aggregation_report(df):
    df_nulls = check_column_names_and_missing_values(df)
    if df_nulls['num_nulls'].sum() == 0:
        descr = "W zbiorze danych nie ma braków danych."
    else:
        descr = f"W zbiorze danych jest łącznie {df_nulls['num_nulls'].sum()} braków danych."
    return descr

def one_hot_encode_columns(df, columns_list):
    df = pd.get_dummies(df, columns=columns_list, prefix=columns_list, drop_first=True)
    return df

def find_duplicates(df):
    duplicates = df[df.duplicated(keep=False)]
    if not duplicates.empty:
        descr = "Znaleziono zduplikowane obserwacje:"
        print(duplicates)
    else:
        descr = "Nie znaleziono zduplikowanych obserwacji."
    return (descr, duplicates)


def unique_values(df, num_of_unique_values):
    for col in df.columns:
        if df[col].dtype in ['object']:
            unique_values = sorted(df[col].unique())
            if len(unique_values) <= num_of_unique_values:
                print(f"{col}: {df[col].dtype}, {unique_values}\n")