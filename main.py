import sys
from src.nearest_neighbor import NearestNeighbor
from src.spotify import Spotify
from src.echonest import Echonest

spotify_uri = "" # the Spotify URI to classify
n_training_data = 10 # the number of samples to train with

if len(sys.argv) > 1:
    spotify_uri = sys.argv[1]
    if len(sys.argv) > 2:
        n_training_data = int(sys.argv[2])
else:
    print("Please pass a Spotify Track URI (eg: spotify:track:3lByrqVGjmURiNbfeSucjb)")
    sys.exit()

print("Classifying " + str(spotify_uri) + " using " + str(n_training_data) + " training samples")

# retrieve the Spotify data to verify the correct track is being used
sp = Spotify()
sp_track = sp.load_track(spotify_uri)
print("Using track '" + sp_track['name'] + "'")

# retrieve the track audio summary
en = Echonest()
en_track = en.track_attributes(sp_track).values()
print("Danceability: " + str(en_track[0])) # printed to verify classification

# find the nearest neighbor based on all of the data aside from the classification
nn = NearestNeighbor()
index = nn.nearest_neighbor_index(en_track[1:])

# print the closest track and it's classification
print(nn.index_to_track_title(index))
print(nn.index_to_track_classification(index))
print(sp.spotify_uri_to_url(nn.index_to_track_spotify_uri(index)))
