from common.utils import weighted_rating
from common.constants import RECO_STANDARD

def get_reco_of_popularity(df_meta):
    # 인기도 추천 스코어를 만들어서 정렬하고 전달
    df_meta = df_meta[['title', 'vote_average', 'vote_count']].copy()
    m = df_meta['vote_count'].quantile(RECO_STANDARD.PERCENTILE) # 평점을 부여하기 위한 최소 평가 수(즉, 상위 60%에 해당하는 평가 수만 인정)
    C = df_meta['vote_average'].mean() # 전체 영화의 평균 평점
    df_meta['score'] = df_meta.apply(lambda x: weighted_rating(x, m, C), axis = 1)
    sorted_meta = df_meta.sort_values(by = 'score', ascending = False)

    return sorted_meta['title'].values
    