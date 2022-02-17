from apiclient.discovery import build
from keys import *

resource = build("customsearch", 'v1', developerKey=kaf_api_key).cse()


def searchkaf(query, number=1):
	result = resource.list(q=query, cx='d895f3626a5b49f12').execute()
	return (result['items'][0]['title'] + ": " + result['items'][0]['link'])