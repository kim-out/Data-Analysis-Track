import pandas as pd 

def load_data(data_path:str, is_meta:bool=False)->pd.DataFrame:
    if is_meta:
        return pd.read_csv(data_path, low_memory=False)
    else:
        return pd.read_csv(data_path, sep=',', engine='c', header='infer')


