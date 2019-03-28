import sys
import tweepy
import configparser

if __name__ == "__main__":

	# get stdin
	search_word = sys.argv[1]

	config = configparser.ConfigParser()
	config.read('config.ini')
	API_KEYS = config['api_key']
	ACCESS_KEYS = config['access_key']
	API_SETTING = config['api_setting']

	auth = tweepy.OAuthHandler(API_KEYS['API_KEY'], API_KEYS['SECRET_API_KEY'])
	auth.set_access_token(ACCESS_KEYS['ACCESS_TOKEN'], ACCESS_KEYS['SECRET_ACCESS_TOKEN'])

	tweepy_api = tweepy.API(auth)

	results = tweepy_api.search(q=search_word, count=API_SETTING['SEARCH_LIMIT'])

	for i, result in enumerate(results, start=1):
		print('processing...{} of {}'.format(len(results), i))
		user_id = result.user._json['screen_name']
		print('user_id', user_id)
		tweepy_api.create_friendship(user_id)
