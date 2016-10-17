import json
import random
import subprocess
import urllib2
import urllib

def getJson(url, queryParams):
  response = urllib2.urlopen(url + '?' + urllib.urlencode(queryParams))
  return json.load(response)

def getGif(gifQuery):
  baseUrl = 'http://api.giphy.com/v1/gifs/search'
  limit = 100
  queryParams = {
    'q': gifQuery,
    # Public Giphy key
    # See here for more info: https://github.com/Giphy/GiphyAPI#public-beta-key
    # Giphy confirmed it is fine to use it in this step context
    'api_key': 'dc6zaTOxFJmzC',
    'limit': limit,
  }

  data = getJson(baseUrl, queryParams)['data']

  return data[random.randint(0,len(data) - 1)]['images']['fixed_height']['url']

def addEnvironmentVariable(key, value):
  subprocess.call(['envman', 'add', '--key', key, '--value', value])

gifName = random.choice(['such wow', 'awesome', 'shipit', 'yes', 'panda', 'cat', 'hell yeah', 'applaud', 'lgtm', 'surprise', 'suprise motherfucker', 'yeah bitches', 'high five', 'legendary', 'lil bub'])
gif = getGif(gifName)

addEnvironmentVariable('GIF_URL', gif)
