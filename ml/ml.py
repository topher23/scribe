from ml.NN import NN
from ml.DT import DT
from ml.KNN import KNN
from sklearn.model_selection import train_test_split
import pandas as pd



class ml():

    def __init__(self, data):
        self.X = data.drop('outcome_type', 1).copy().values
        self.Y = data['outcome_type'].copy().values
        x_train, x_test, y_train, y_test = train_test_split(self.X, self.Y, random_state=0, test_size=0.25)

        self.nn_learner = NN(x_train, x_test, y_train, y_test, self.X, self.Y, "data")
        self.dt_learner = DT(x_train, x_test, y_train, y_test, self.X, self.Y, "data")
        self.knn_learner = DT(x_train, x_test, y_train, y_test, self.X, self.Y, "data")

        self.nn_best = None
        self.dt_best = None
        self.knn_best = None

    def train_ml(self):
        self.nn_best = self.nn_learner.find_optimal()
        self.dt_best = self.dt_learner.find_optimal()
        self.knn_best = self.knn_learner.find_optimal()

    def predict_ml(self, x_data):
        return self.nn_best.predict(x_data)
        #return self.dt_best.predict(x_data)
        #return self.knn_best.predict(x_data)
