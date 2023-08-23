import numpy as ny
import networkx as nx

class Network_input():

    def __init__(self, satellite_time):
        self.matrix = ny.loadtxt('G:/code/pythonProject/Deep_Q-Learning/starlink_AER/result'+str(satellite_time)+'.csv', delimiter=",", skiprows=0)
    def graphy_generate(self):
        G = nx.Graph()
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if self.matrix[i][j] > 1:
                    G.add_edge(i, j)
        return G

