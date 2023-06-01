
def get_reco_of_popularity(df_meta):
    # 인기도 추천 스코어를 만들어서 정렬하고 전달 
    sorted_meta = df_meta[['title', 'vote_average', 'vote_count']].sort_values(by = 'vote_average', ascending = False)
    return sorted_meta[sorted_meta.vote_count > 1000]['title'].values
    