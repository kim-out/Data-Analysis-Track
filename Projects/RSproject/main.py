import argparse
from services.process import process_recommendation

def recommend(args):
    recommendation = {
        'contents': None,
        'reco_type': None,
        'user_id': args.user_id
    }
    return process_recommendation(recommendation) 

if __name__ == "__main__":
    print('run')
    try:
        parser = argparse.ArgumentParser() 
        parser.add_argument("--user_id", type=int)
        args = parser.parse_args()

        recommendation = recommend(args)
        print('####################################')
        print(recommendation)
        print('####################################')
    except Exception as e:
        print('####################################')
        print(e)
        print('####################################')






