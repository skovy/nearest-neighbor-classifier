from .nearest_neighbor import NearestNeighbor
from .spotify import Spotify
from .echonest import Echonest

class SpotifyNearestNeighbor:
    # spotify_uri - the Spotify URI to find the nearest neighbors
    # n_training_data - the number of samples to use
    # n_neighbors - the number of neighbors to find
    def __init__(self, spotify_uri, n_training_data = 10, n_neighbors = 1):
        self.spotify_uri = spotify_uri
        self.n_training_data = n_training_data
        self.n_neighbors = n_neighbors

    def perform(self):
        en = Echonest()
        en_track = en.track_attributes(self.spotify_uri).values()

        nn = NearestNeighbor(self.n_training_data, self.n_neighbors)

        distances, indices = nn.nearest_neighbors(en_track)

        db_indices = []
        for index in indices[0]:
            print nn.data[index][2], nn.data[index][0]
            db_indices.append(nn.data[index][2])

        return db_indices;
