import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep

SPOTIPY_CLIENT_ID = 'f049ec6107994ffb84fb6b29c140cf49'
SPOTIPY_CLIENT_SECRET = 'd6d19bc2c335413abcb71006196ea2a5'
REDIRECT_URI = 'http://localhost:8888/'
SCOPES = ['user-read-currently-playing']


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=SCOPES))


def get_current_track():
    currently_playing = sp.currently_playing()
    return currently_playing.get('item').get('name')