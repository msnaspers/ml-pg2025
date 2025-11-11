import pandas as pd
import kagglehub
import os
def rename_columns_snake_case(dataframe):
    dataframe = dataframe.copy()
    dataframe.columns = [col.lower().replace(" ", "_").replace("(", "_").replace(")", "")  for col in dataframe.columns]
    return dataframe

def data_reader(path: str):
    parts = [os.path.dirname(path) + "/", os.path.basename(path)]
    dataset_path = kagglehub.dataset_download(parts[0].rstrip("/"))
    return pd.read_csv(os.path.join(dataset_path, parts[1]))
