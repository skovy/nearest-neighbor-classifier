from src.nearest_neighbor import NearestNeighbor

nn = NearestNeighbor()
index = nn.nearest_neighbor_index([-4.74700000, 0.65203858, 0.05823739, 0.06729183, 0.00258966, 0.00000007])
print(nn.data[index][0])
print(nn.data[index][1])
