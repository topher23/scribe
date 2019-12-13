from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import numpy as np
import sklearn.model_selection as ms
from sklearn.tree import DecisionTreeClassifier
from ml.Learner import Learner


class DT(Learner):

    def __init__(self, X_train, X_test, y_train, y_test, X, y, problem):
        # Constants for grid search, learning curve, and validation curve
        self.verbosity = 0
        self.cv = 7
        self.train_sizes = np.arange(0.05, 1, 0.01)
        self.scoring = "accuracy"
        self.parallels = -1

        # varying values for Params
        self.max_depth = np.arange(1, 21, 1)
        self.max_leaf_nodes = np.arange(2, 21, 1)
        self.params = {'DT__max_depth': self.max_depth,'DT__max_leaf_nodes': self.max_leaf_nodes}
        self.pipe = Pipeline([('Scale',StandardScaler()),
                              ('DT', DecisionTreeClassifier( random_state=99))])

        super().__init__(X_train, X_test, y_train, y_test, X, y, self.pipe, "DT", problem)

    def find_optimal(self):
        grid_search = ms.GridSearchCV(self.pipe, n_jobs=self.parallels, param_grid=self.params, refit=True, cv=self.cv,
                                      verbose=self.verbosity, scoring=self.scoring)
        grid_search.fit(self.X_train, self.y_train)
        train_score = grid_search.score(self.X_train, self.y_train)
        print("Train score of " + str(train_score) + " for DT "+ self.problem)
        test_score = grid_search.score(self.X_test, self.y_test)
        print("Test score of " + str(test_score) + " for DT "+ self.problem)
        return grid_search.best_estimator_