#spotify api
#building


import json
import urllib.parse
import urllib.request


BASE_SEARCH_URL = 'https://api.spotify.com/v1/search?'
#https://api.spotify.com/v1/search?q=track:viva+la+vida+artist:coldplay&type=track&limit=1
BASE_TRACK_URL = 'https://api.spotify.com/v1/tracks/'


def build_search_url(info: tuple):
    parameters = []
    parameters.append(('limit', 1))
    parameters.append(("type", "track"))

    artist = info[0].replace(" ", "+")
    track = info[1].replace(" ", "+")
    package = "&q=" + "track:" + track + "+artist:" + artist

    return BASE_SEARCH_URL + urllib.parse.urlencode(parameters) + package


    
def get_json(url: str)->dict:
    response = None

    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')

        return json.loads(json_text)

    finally:
        if response != None:
            response.close()


def get_id(json: dict)->str:
    '''returns the id of the song'''
    return json["tracks"]["items"][0]["id"]


def build_track_url(track_id: str)->str:
    return BASE_TRACK_URL + track_id


def get_popularity(json: dict)->str:
    return json["popularity"] 





#get_id(get_json(build_search_url(('coldplay', 'viva la vida'))))
    

