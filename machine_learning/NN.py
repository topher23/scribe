from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import numpy as np
import sklearn.model_selection as ms
from sklearn.neural_network import MLPClassifier
from machine_learning.Learner import Learner


class NN(Learner):

    def __init__(self, X_train, X_test, y_train, y_test, X, y, problem):
        # Constants for grid search, learning curve, and validation curve
        self.parallels = -1
        self.cv = 7
        # self.cv = ms.StratifiedShuffleSplit(n_splits=5)
        #self.train_sizes = np.arange(0.05, 1, 0.01)
        #default is below
        self.train_sizes = np.linspace(0.1, 1.0, 5)
        self.verbosity = 0
        self.scoring = "accuracy"

        # varying values for Params
        self.hidden_layer_sizes =[(3,), (3,3,), (3,3,3), (6,), (6,6,), (6,6,6), (12,), (12,12,), (12,12,12)]
        self.alpha = np.arange(0, 9, 0.1)
        #for quicker, use below alpha
        # self.alpha = np.arange(0, 9, 1)
        self.params = {'MLP__alpha': self.alpha, 'MLP__hidden_layer_sizes': self.hidden_layer_sizes}
        self.pipe = Pipeline([('Scale',StandardScaler()),
                              ('MLP',MLPClassifier(random_state=99, max_iter=2500,early_stopping=True))])
        super().__init__(X_train, X_test, y_train, y_test, X, y, self.pipe, "NN", problem)

    def find_optimal(self):
        grid_search = ms.GridSearchCV(self.pipe, n_jobs=self.parallels, param_grid=self.params, refit=True, cv=self.cv,
                                      scoring=self.scoring, verbose=self.verbosity)
        grid_search.fit(self.X_train, self.y_train)
        train_score = grid_search.score(self.X_train, self.y_train)
        print("Train score of " + str(train_score) + " for NN " + self.problem)
        test_score = grid_search.score(self.X_test, self.y_test)
        print("Test score of " + str(test_score) + " for NN " + self.problem)
        return grid_search.best_estimator_