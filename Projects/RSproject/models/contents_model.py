from common.utils import weighted_rating
from common.constants import RECO_STANDARD
from ast import literal_eval
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.metrics.pairwise import cosine_similarity

def get_reco_of_contents(df_meta, df_hist, df_ratings):
    df_meta = df_meta[['id','title', 'genres', 'vote_count', 'vote_average']].copy()

    m = df_meta['vote_count'].quantile(RECO_STANDARD.PERCENTILE)
    C = df_meta['vote_average'].mean()
    df_meta['score'] = df_meta.apply(lambda x: weighted_rating(x, m, C), axis = 1)

    df_meta['genres'] = df_meta['genres'].map(literal_eval).map(lambda x: [i['name'] for i in x]).map(lambda x: (' ').join(x))
    
    count_vect = CountVectorizer(min_df=0, ngram_range=(1,2)) 

    genre_mat = count_vect.fit_transform(df_meta['genres'])
    genre_sim = cosine_similarity(genre_mat, genre_mat)
    genre_sim_sorted_ind = genre_sim.argsort()[:, ::-1] # 유사도가 높은 순서로 정렬 
    
    
    # df_hist의 영화 중 평점이 가장 높은 영화 5개와 유사한 영화를 20개 씩 가져옴(중복 제거)
    df_hist = df_hist[['movieId','rating']].sort_values(by='rating', ascending = False)[:5].copy()
    user_favor = df_meta[df_meta['id']==df_hist['movieId']]['title']

    
    pass 
