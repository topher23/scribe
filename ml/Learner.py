from abc import ABC, abstractmethod
from time import clock

import numpy as np
import sklearn.model_selection as ms
import matplotlib.pyplot as plt


class Learner(ABC):

    def __init__(self, X_train, X_test, y_train, y_test, X, y, pipe, learner, problem):
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test
        self.X = X
        self.y = y
        self.learner = learner
        self.problem = problem
        self.pipe = pipe

        #super().__init__()

    @abstractmethod
    def find_optimal(self):
        pass

    @abstractmethod
    def generate_learning_plot(self, grid_search):
        pass

    @abstractmethod
    def generate_complexity_model_plots(self, grid_search):
        pass