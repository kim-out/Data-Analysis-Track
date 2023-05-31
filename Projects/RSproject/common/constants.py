import enum 

class RECO_TYPE(enum.Enum):
    POPULARITY = (enum.auto, '인기도 추천')
    CONTENTS = (enum.auto, 'Contents Based Filtering')
    COLLABORATIVE = (enum.auto, 'Collaborative Filtering')

class RECO_STANDARD(enum.Enum):
    HEAVY_USER = (enum.Enum, 10, '최소 해비 사용자 기준')
    RECO_SIZE = (enum.Enum, 5, '추천 컨텐츠 수')

class PATH_INFO(enum.Enum):
    DATA_RATINGS = (enum.Enum, 'C:/python/Projects/RSproject/data/ml-1m/ratings.csv', '데이터 위치 정보')
    DATA_META = (enum.Enum, 'C:/python/Projects/RSproject/data/ml-1m/movies_metadata.csv', '메타 데이터 위치 정보')

    
