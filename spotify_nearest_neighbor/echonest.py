from pyechonest import track

class Echonest:
    def track_attributes(self, spotify_uri):
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
            return { 'error': "Error occurred finding track '" + spotify_uri + "'." }
