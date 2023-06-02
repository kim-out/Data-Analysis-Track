import pandas as pd 

def load_data(data_path:str, is_meta:bool=False)->pd.DataFrame:
    if is_meta:
        return pd.read_csv(data_path, low_memory=False)
    else:
        return pd.read_csv(data_path, sep=',', engine='c', header='infer')

def weighted_rating(record, m, C):

    v = record['vote_count'] # 영화에 평가를 매긴 횟수 
    R = record['vote_average'] # 영화의 평균 평점

    return ( (v/(v+m)) * R ) + ( (m/(m+v)) * C ) # 가중 평점 계산 식 

