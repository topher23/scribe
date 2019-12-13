from machine_learning.NN import NN
from machine_learning.DT import DT
from machine_learning.KNN import KNN
from sklearn.model_selection import train_test_split
import pandas as pd

class ml():

    def __init__(self, data, arg):
        self.X = data.drop('Invested', 1).copy().values
        self.Y = data['Invested'].copy().values
        x_train, x_test, y_train, y_test = train_test_split(self.X, self.Y, random_state=0, test_size=0.25)



        if arg == "dt":
            self.learner = DT(x_train, x_test, y_train, y_test, self.X, self.Y, "data")
        elif arg == "nn":
            self.learner = NN(x_train, x_test, y_train, y_test, self.X, self.Y, "data")
        else:
            self.learner = KNN(x_train, x_test, y_train, y_test, self.X, self.Y, "data")

        self.best = None
        self.best = None
        self.best = None

    def train_ml(self):
        self.best = self.learner.find_optimal()

    def predict_ml(self, x_data):
        return self.best.predict(x_data)


d = pd.read_csv("../Models/companies.csv")
mach = ml(d, dt)
mach.train_ml()