from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import numpy as np
import sklearn.model_selection as ms
from sklearn.neighbors import KNeighborsClassifier
from machine_learning.Learner import Learner


class KNN(Learner):

    def __init__(self, X_train, X_test, y_train, y_test, X, y, problem):
        # Constants for grid search, learning curve, and validation curve
        self.cv = 7
        # self.cv = ms.StratifiedShuffleSplit(n_splits=5)
        self.train_sizes = np.arange(0.05, 1, 0.01)
        self.verbosity = 0
        self.scoring = "accuracy"
        self.parallels = -1

        # varying values for Params
        self.n_neighbors = np.arange(1, 30, 1)
        self.metric = ['manhattan', 'minkowski', 'euclidean', 'hamming', 'chebyshev']
        self.params = {'KNN__n_neighbors': self.n_neighbors, 'KNN__metric': self.metric}
        self.pipe = Pipeline([('Scale', StandardScaler()),
                          ('KNN', KNeighborsClassifier())])

        super().__init__(X_train, X_test, y_train, y_test, X, y, self.pipe, "KNN", problem)

    def find_optimal(self):
        grid_search = ms.GridSearchCV(self.pipe, n_jobs=self.parallels, param_grid=self.params, refit=True, cv=self.cv,
                                      scoring=self.scoring, verbose=self.verbosity)
        grid_search.fit(self.X_train, self.y_train)
        train_score = grid_search.score(self.X_train, self.y_train)
        print("Train score of " + str(train_score) + " for KNN " + self.problem)
        test_score = grid_search.score(self.X_test, self.y_test)
        print("Test score of " + str(test_score) + " for KNN " + self.problem)
        return grid_search.best_estimator_