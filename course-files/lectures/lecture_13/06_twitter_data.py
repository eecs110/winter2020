import urllib.request
import json
import pprint

# Write a program that only prints the text of the most popular 
# tweet (given the search results).

search_term = input('Please enter a search term: ')
url = 'https://www.apitutor.org/twitter/simple/1.1/search/tweets.json?q='
url += search_term
request = urllib.request.urlopen(url)
statuses = json.loads(request.read().decode())

pprint.pprint(statuses, depth=2) # The first value is another dictionary, the second is a list of dictionaries