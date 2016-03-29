from pyechonest import track

class Echonest:
    def track_attributes(self, spotify_track):
        spotify_uri = spotify_track['uri']
        spotify_track_name = spotify_track['name']
        spotify_album_name = spotify_track['album']['name']
        spotify_album_cover_url = spotify_track['album']['images'][0]['url']
        try:
            t = track.track_from_id(spotify_uri)
            res = {
                'danceability': t.danceability,
                'loudness': t.loudness,
                'energy': t.energy,
                'speechiness': t.speechiness,
                'liveness': t.liveness,
                'acousticness': t.acousticness,
                'instrumentalness': t.instrumentalness
            }
            return res
        except:
            return { 'error': "Error occurred finding track '" + spotify_uri + "' using Echonest." }
