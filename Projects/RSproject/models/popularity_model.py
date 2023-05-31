
def get_reco_of_popularity(DATA_RATINGS):
    # 인기도 추천 스코어를 만들어서 정렬하고 전달 


    data = DATA_RATINGS[['id','original_title','vote_average']]
    data['score'] = data.apply(lambda x: x.vote_average)
    pass 