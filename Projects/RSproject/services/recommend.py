
from models.popularity_model import get_reco_of_popularity
from models.contents_model import get_reco_of_contents
from models.collaborative_model import get_reco_of_collaborative

def __recommend_without_hist(reco_list, hist_list, reco_size):
    # 기존 시청한 컨텐츠 제외 
    reco_set = set(reco_list) - set(hist_list)
    return list(reco_set)[:reco_size]

def recommend_popularity(df_ratings, reco_size):
    pass 
    # 1. get_reco_of_popularity를 사용해서 추천 정렬 리스트(데이터 프레임)
    # 2. 추천 크기 만큼 짤라서 전달  


def recommend_contents(df_ratings, df_hist, reco_size):
    pass 
    # get_reco_of_contents를 사용해서 추천 
    # __recommend_without_hist 사용


def recommend_collaborative(df_ratings, df_hist, reco_size):
    pass 
    # get_reco_of_collaborative를 사용해서 추천 
    # __recommend_without_hist 사용

