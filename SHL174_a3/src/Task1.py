import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsClassifier
import warnings
warnings.filterwarnings('ignore')

class Task1:
    # please feel free to create new python files, adding functions and attributes to do training, validation, testing

    def __init__(self):
        print("================Task 1================")
        return

    # Linear regression is the first model
    def model_1_run(self):
        print("Model 1:")
        # Train the model 1 with your best hyper parameters (if have) and features on training data.
        # load data
        x,y = self.loadData("train")
        # do the one-hot encoding for all category features
        x = pd.get_dummies(x)

        # use 10 fold cross validation to evaluate linear regression
        reg = LinearRegression(fit_intercept=True, normalize=True)
        scores = cross_val_score(reg, x, y, cv=10)
        # print("LR MSE", scores.mean())
        # use lasso to do the feature selection
        lasso = Lasso()
        # use 10 fold cross validation to evaluate linear regression with lasso
        scores = cross_val_score(lasso, x, y, cv=10)
        # print("Lasso MSE", scores.mean())
        # use Ridge to do the feature selection

        # use 10 fold cross validation to find the best alpha for ridge
        max_score = -float("inf")
        best_a = 0
        for a in np.arange(0, 1, 0.1):
            ridge = Ridge(alpha=a)
            loss = cross_val_score(ridge, x, y, cv=10).mean()
            if loss>max_score:
                max_score = loss
                best_a = a
        # print("Ridge MSE", max_score)

        # based on the score, Ridge is the best
        # train Ridge with training set
        ridge = Ridge(alpha=best_a).fit(x, y)

        # Evaluate learned model on testing data, and print the results.
        x_test, y_test = self.loadData("test")
        x_test = pd.get_dummies(x_test)
        miss_columns = set(x) - set(x_test)
        for col in miss_columns:
            x_test[col] = 0
        y_pred = ridge.predict(x_test)
        print("Mean squared error\t" + str(mean_squared_error(y_test, y_pred)))
        return

    # decision tree model
    def model_2_run(self):
        print("--------------------\nModel 2:")
        # Train the model 2 with your best hyper parameters (if have) and features on training data.
        # load data
        x, y = self.loadData("train")
        # do the one-hot encoding for all category features
        x = pd.get_dummies(x)
        max_score = -float("inf")
        best_n = 0
        for i in range(150, 200, 10):
            rfr = RandomForestRegressor(n_estimators=i, random_state=90)
            score = cross_val_score(rfr, x, y, cv=10).mean()
            if score>max_score:
                max_score = score
                best_n = i

        rfr = RandomForestRegressor(n_estimators=best_n, random_state=90).fit(x,y)
        # Evaluate learned model on testing data, and print the results.
        x_test, y_test = self.loadData("test")
        x_test = pd.get_dummies(x_test)
        miss_columns = set(x) - set(x_test)
        for col in miss_columns:
            x_test[col] = 0
        y_pred = rfr.predict(x_test)
        print("Mean squared error\t" + str(mean_squared_error(y_test, y_pred)))
        return

    # use pandas to load data
    def loadData(self, type):
        if type == "train":
            data = pd.read_table('../data/assign3_students_train.txt', header=None, sep="\t")
            data.columns = ["school", "sex", "age", "address", "famsize", "pstatus", "medu", "fedu", "mjob", "fjob",
                            "reason", "guardian", "traveltime", "studytime", "failures", "edusupport", "nursery",
                            "higher",
                            "internet", "romantic", "famrel", "freetime", "goout", "dalc", "walc", "health", "absences",
                            "g3"]
        else:
            data = pd.read_table('../data/assign3_students_test.txt', header=None, sep="\t")
            data.columns = ["school", "sex", "age", "address", "famsize", "pstatus", "medu", "fedu", "mjob", "fjob",
                            "reason", "guardian", "traveltime", "studytime", "failures", "edusupport", "nursery",
                            "higher",
                            "internet", "romantic", "famrel", "freetime", "goout", "dalc", "walc", "health", "absences",
                            "g3"]
        x = data.iloc[:, 0:27]
        y = data[["g3"]]
        return x, y
