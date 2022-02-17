from apiclient.discovery import build
from keys import *

resource = build("customsearch", 'v1', developerKey=kaf_api_key).cse()


def searchkaf(query, number=1):
	results = []
	result = resource.list(q=query, cx='d895f3626a5b49f12').execute()
	for x in range(int(number)):
		results.append(result['items'][x]['title'] + ": " + result['items'][x]['link'])
	return results
