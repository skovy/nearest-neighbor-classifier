from sklearn.neighbors import NearestNeighbors
from src.track_data import TrackData
import numpy as np

class NearestNeighbor:
    def __init__(self):
        self.td = TrackData()
        self.data = []
        self.load_data()
        self.neighbors = self.train()

    # load the track data from the database
    def load_data(self):
        self.data = self.td.retrieve_data(10)

    # train with our dataset
    def train(self):
        training_data = []
        for i, row in enumerate(self.data):
            training_data.append([])
            for col in row[2:]:
                val = 0
                if col != None:
                    val = float(col)
                training_data[i].append(val)

        training_data = np.array(training_data)
        return NearestNeighbors(n_neighbors=1, algorithm='auto').fit(training_data)

    def nearest_neighbor_index(self, vector):
        return self.neighbors.kneighbors([vector], return_distance=False)[0][0]
