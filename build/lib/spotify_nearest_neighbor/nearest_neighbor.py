from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import normalize
from .track_data import TrackData
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
        self.training_data = []
        self.neighbors = None

        # load the training data
        self.load_data()

    # turn an index into a track title
    def index_to_track_title(self, index):
        return self.data[index][0]

    # turn an index into track spotify_uri
    def index_to_track_spotify_uri(self, index):
        return self.data[index][1]

    # turn an index into track db id
    def index_to_id(self, index):
        return self.data[index][2]

    def get_sample_with_id(self, id):
        for i, sample in enumerate(self.data):
            if sample[2] == id:
                return self.training_data[i]

    # load the track data from the database
    def load_data(self):
        self.data = self.td.retrieve_data(self.n_training_data)

    # make the data valid to what we need
    def validate_data(self, value):
        if value != None:
            return float(value)
        return 0

    # train with our dataset
    def train(self, vector):
        # remove the track title and the classification and convert remaining
        # values to floats
        training_data = []
        for i, row in enumerate(self.data):
            training_data.append([])
            for j, col in enumerate(row[3:]): # ignore meta data
                training_data[i].append(self.validate_data(col))

        i = len(training_data)
        training_data.append([])
        for col in vector:
            training_data[i].append(self.validate_data(col))

        self.training_data = normalize(np.array(training_data), norm = 'l2', axis = 1)
        v = self.training_data[len(self.training_data) - 1]
        self.training_data = self.training_data[:-1]
        self.neighbors = NearestNeighbors(n_neighbors=self.n_neighbors, algorithm='auto').fit(self.training_data)
        return v

    def nearest_neighbors(self, vector):
        v = self.train(vector)
        print v
        return self.neighbors.kneighbors([v])

    # retrieve the index for the nearest neighbor to the vector passed in
    def nearest_neighbor_index(self, vector):
        return self.neighbors.kneighbors([vector], return_distance=False)[0][0]
