def rename_columns_snake_case(dataframe):
    dataframe = dataframe.copy()
    dataframe.columns = [col.lower().replace(" ", "_").replace("(", "_").replace(")", "")  for col in dataframe.columns]
    return dataframe

