import sys
from src.nearest_neighbor import NearestNeighbor
from src.spotify import Spotify
from src.echonest import Echonest

spotify_uri = "" # the Spotify URI to classify
n_training_data = 10 # the number of samples to train with
n_neighbors = 1 # the number of neighbors to classify with

if len(sys.argv) > 1:
    spotify_uri = sys.argv[1]
    if len(sys.argv) > 2:
        n_training_data = int(sys.argv[2])
    if len(sys.argv) > 3:
        n_neighbors = int(sys.argv[3])
else:
    print("Please pass a Spotify Track URI (eg: spotify:track:3lByrqVGjmURiNbfeSucjb)")
    sys.exit()

print("Classifying " + str(spotify_uri) + " using " + str(n_training_data) + " training samples and " + str(n_neighbors) + " neighbors")

# retrieve the Spotify data to verify the correct track is being used
sp = Spotify()
sp_track = sp.load_track(spotify_uri)

# retrieve the track audio summary
en = Echonest()
en_track = en.track_attributes(sp_track).values()

print("Using track '" + sp_track['name'] + "' with danceability of " + str(en_track[0]))

# find the nearest neighbor based on all of the data aside from the classification
nn = NearestNeighbor(n_training_data, n_neighbors)
index = nn.nearest_neighbor_index(en_track[1:])

# print the k closest neightbors and distances
distances, indices = nn.nearest_neighbors(en_track[1:])
for distance, index in zip(distances[0], indices[0]):
    print("[{0}] '{1}' at distance {2} classified as '{3}' - {4}").format(index, nn.index_to_track_title(index), distance, nn.index_to_track_classification(index), sp.spotify_uri_to_url(nn.index_to_track_spotify_uri(index)))
