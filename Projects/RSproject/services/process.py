
from common.utils import load_data
from common.constants import PATH_INFO, RECO_TYPE, RECO_STANDARD
from .recommend import recommend_popularity, recommend_contents, recommend_collaborative

def __check_recommendation(recommendation, df_hist, reco_size):

    # 추천 컨텐츠 수 확인 
    assert reco_size == len(recommendation['contents'])
    # 시청 컨텐츠 추천 유무 확인
    pass 
    # 추천 종류 확인 
    pass 
    # 추천 사용자 아이디 확인 
    pass 

    return recommendation

def process_recommendation(recommendation, reco_size=RECO_STANDARD.RECO_SIZE.value[1]):

    # 전체 사용자 이력 정보 조회
    df_ratings = load_data(PATH_INFO.DATA_RATINGS.value[1]) 
    df_meta = load_data(PATH_INFO.DATA_META.value[1])

    # 추천 사용자 이력 정보 조회 
    df_hist = df_ratings[df_ratings['userId'] == int(recommendation['user_id'])]

    # 추천 사용자 이력 정보를 바탕으로 추천 
    len_hist = len(df_hist)

    # 이력이 없으면 popularity
    if not len_hist:
        recommendation['reco_type'] = RECO_TYPE.POPULARITY.name
        recommendation['contents'] = recommend_popularity(df_meta, reco_size)
    
    # heavy user면 contents based 
    elif len_hist > RECO_STANDARD.HEAVY_USER.value[1]:
        recommendation['reco_type'] = RECO_TYPE.CONTENTS.name
        recommendation['contents'] = recommend_contents(df_ratings, df_hist, reco_size) 
    
    # 나머지는 collaborative
    else:
        recommendation['reco_type'] = RECO_TYPE.COLLABORATIVE.name
        recommendation['contents'] = recommend_collaborative(df_ratings, df_hist, reco_size) 
    
    return __check_recommendation(recommendation, df_hist, reco_size)

    

