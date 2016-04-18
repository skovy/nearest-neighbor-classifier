from pyechonest import track

class Echonest:
    def track_attributes(self, spotify_uri):
        try:
            t = track.track_from_id(spotify_uri)
            res = [
                t.danceability,
                t.loudness,
                t.energy,
                t.speechiness,
                t.liveness,
                t.acousticness,
                t.instrumentalness
            ]
            return res
        except:
            return { 'error': "Error occurred finding track '" + spotify_uri + "'." }
