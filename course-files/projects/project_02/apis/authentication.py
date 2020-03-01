import traceback
import sys
import urllib.request
from urllib.request import urlopen
import json
from apis import utilities

try:
    from apis import my_token
    API_TUTOR_TOKEN = my_token.API_TUTOR_TOKEN
except:
    raise Exception('Go to Canvas to get the token. Then replace lines 1-5 with API_TUTOR_TOKEN = "THE_CLASS_TOKEN"')



def get_token(url):
    try:
        response = urlopen(url + '?auth_manager_token=' + API_TUTOR_TOKEN)
        data = response.read()
        results = data.decode('utf-8', 'ignore')
        return json.loads(results)['token']
    except urllib.error.HTTPError as e:
        # give a good error message:
        error = utilities.get_error_message(e, url)
    raise Exception(error)