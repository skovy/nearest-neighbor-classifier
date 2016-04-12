from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import normalize
from src.track_data import TrackData
import numpy as np

class NearestNeighbor:
    # n_training_data - the number of samples to use as the training data
    # n_neighbors - the number of neighbors to use
    def __init__(self, n_training_data = 10, n_neighbors = 1):
        # configurations for training
        self.n_training_data = n_training_data
        self.n_neighbors = n_neighbors

        self.td = TrackData() # database used to load the training data
        self.data = [] # data structure to hold all of the training data

        # load the training data
        self.load_data()
        self.neighbors = self.train()

    # turn an index into a track title
    def index_to_track_title(self, index):
        return self.data[index][0]

    # turn an index into track spotify_uri
    def index_to_track_spotify_uri(self, index):
        return self.data[index][1]

    # turn an index into track classification
    def index_to_track_classification(self, index):
        return self.data[index][2]

    # load the track data from the database
    def load_data(self):
        self.data = self.td.retrieve_data(self.n_training_data)

    # train with our dataset
    def train(self):
        # remove the track title and the classification and convert remaining
        # values to floats
        training_data = []
        for i, row in enumerate(self.data):
            training_data.append([])
            for col in row[3:]:
                val = 0
                if col != None:
                    val = float(col)
                training_data[i].append(val)

        training_data = normalize(np.array(training_data), norm = 'l2', axis = 0)
        return NearestNeighbors(n_neighbors=self.n_neighbors, algorithm='auto').fit(training_data)

    def nearest_neighbors(self, vector):
        vector = normalize(np.array([vector]), norm='l2')
        return self.neighbors.kneighbors(vector)

    # retrieve the index for the nearest neighbor to the vector passed in
    def nearest_neighbor_index(self, vector):
        return self.neighbors.kneighbors([vector], return_distance=False)[0][0]
