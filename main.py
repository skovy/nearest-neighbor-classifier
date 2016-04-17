import sys
from src.nearest_neighbor import NearestNeighbor
from src.spotify import Spotify
from src.echonest import Echonest

spotify_uri = "" # the Spotify URI to classify
n_training_data = 10 # the number of samples to train with
n_neighbors = 1 # the number of neighbors to classify with
index_of_attribute_to_classify = 0

attrs = ["danceability", "loudness", "energy", "speechiness", "liveness", "acousticness", "instrumentalness"]

if len(sys.argv) > 1:
    spotify_uri = sys.argv[1]
else:
    print("Please pass a Spotify Track URI (eg: spotify:track:3lByrqVGjmURiNbfeSucjb)")
    sys.exit()

if len(sys.argv) > 2:
    n_training_data = int(sys.argv[2])
if len(sys.argv) > 3:
    n_neighbors = int(sys.argv[3])
if len(sys.argv) > 4:
    index_of_attribute_to_classify = int(sys.argv[4])

attr = attrs[index_of_attribute_to_classify]

print("Classifying " + str(spotify_uri) + " using " + str(n_training_data) + " training samples and " + str(n_neighbors) + " neighbors")

# retrieve the Spotify data to verify the correct track is being used
sp = Spotify()
sp_track = sp.load_track(spotify_uri)

# retrieve the track audio summary
en = Echonest()
en_track = en.track_attributes(sp_track).values()

print("Using track '" + sp_track['name'] + "' with " + attr + " of " + str(en_track[index_of_attribute_to_classify]))

# find the nearest neighbor based on all of the data aside from the classification
nn = NearestNeighbor(n_training_data, n_neighbors, index_of_attribute_to_classify)

smp = nn.get_sample_with_id(265)
print(smp)
en_track = smp.tolist()

# del en_track[index_of_attribute_to_classify]
index = nn.nearest_neighbor_index(en_track)

# print the k closest neightbors and distances
distances, indices = nn.nearest_neighbors(en_track)
for distance, index in zip(distances[0], indices[0]):
    print("[{0}] '{1}' at distance {2} classified as '{3}' - {4}").format(nn.index_to_id(index), nn.index_to_track_title(index), distance, nn.index_to_track_classification(index), sp.spotify_uri_to_url(nn.index_to_track_spotify_uri(index)))
