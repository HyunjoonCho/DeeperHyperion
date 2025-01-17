import numpy as np


class FeatureDimension:
    """
    Implements a feature dimension of the MAP-Elites algorithm
    """

    def __init__(self, name, feature_simulator, bins):
        """
        :param name: Name of the feature dimension
        :param feature_simulator: Name of the method to evaluate the feature
        :param bins: Array of bins, from starting value to last value of last bin
        """
        self.name = name
        self.feature_simulator = feature_simulator
        self.bins = bins
        self.min = np.inf

    def feature_descriptor(self, map_elite, x):
        """
        Simulate the candidate solution x and record its feature descriptor
        :param map_elite:
        :param x: genotype of candidate solution x
        :return:
        """
        i = map_elite.feature_simulator(self.feature_simulator, x)
        return i



