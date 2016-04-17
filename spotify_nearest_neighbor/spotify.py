import spotipy

class Spotify:
    def __init__(self):
        self.sp = spotipy.Spotify()

    def load_track(self, spotify_uri):
        return self.sp.track(spotify_uri)

    def spotify_uri_to_url(self, spotify_uri):
        return "https://open.spotify.com/track/" + spotify_uri.split(':')[2]
