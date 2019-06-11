import json
import random
import subprocess
import urllib2
import urllib
import sys
import os

def addEnvironmentVariable(key, value):
  subprocess.call(['envman', 'add', '--key', key, '--value', value])

def getJson(url, queryParams):
  url = url + '?' + urllib.urlencode(queryParams)
  addEnvironmentVariable('__GIF_GIPHY_URL_CALL__', url)
  response = urllib2.urlopen(url)

  return json.load(response)

def getGif(gifQuery, apiKey):
  baseUrl = 'https://api.giphy.com/v1/gifs/search'
  limit = 100
  queryParams = {
    'q': gifQuery,
    'api_key': apiKey,
    'limit': limit,
  }

  data = getJson(baseUrl, queryParams)['data']

  return data[random.randint(0,len(data) - 1)]['images']['fixed_height']['url']

gifName = random.choice(os.environ['gif_words'].split(','))
apiKey = os.environ['api_key']
gif = getGif(gifName, apiKey)

addEnvironmentVariable('GIF_URL', gif)
