import pandas as pd
from sklearn.model_selection import cross_val_score
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import warnings
warnings.filterwarnings('ignore')

class Task2:
    # please feel free to create new python files, adding functions and attributes to do training, validation, testing

    def __init__(self):
        print("================Task 2================")
        return

    def print_category_results(self, category, precision, recall, f1):
        print("Category\t" + category + "\tF1\t" + str(f1) + "\tPrecision\t" + str(precision) + "\tRecall\t" + str(
            recall))

    def print_macro_results(self, accuracy, precision, recall, f1):
        print("Accuracy\t" + str(accuracy) + "\tMacro_F1\t" + str(f1) + "\tMacro_Precision\t" + str(
            precision) + "\tMacro_Recall\t" + str(recall))

    # KNN model
    def model_1_run(self):
        print("Model 1:")
        # Train the model 1 with your best hyper parameters (if have) and features on training data.
        # load data
        x, y = self.loadData("train")
        x = pd.get_dummies(x)
        best_score = -float("inf")
        best_k = 0
        for k in range(1,50):
            knn = KNeighborsClassifier(n_neighbors=k)
            score = cross_val_score(knn,x,y, cv=10).mean()
            if score>best_score:
                best_score = score
                best_k = k
        # print(best_k)
        knn = KNeighborsClassifier(n_neighbors= best_k).fit(x,y)

        # Evaluate learned model on testing data, and print the results.
        x_test,y_test = self.loadData("test")
        x_test = pd.get_dummies(x_test)
        miss_columns = set(x) - set(x_test)
        for col in miss_columns:
            x_test[col] = 0
        y_pred = knn.predict(x_test)
        matrix = confusion_matrix(y_test,y_pred)
        categories = ["teacher", "health", "service", "at_home", "other"]
        # print(matrix)
        precisions = []
        recalls = []
        f1s = []
        for i in range(len(categories)):
            precisions.append(matrix[i][i]/(sum(matrix[:, i])))
            recalls.append(matrix[i][i]/(sum(matrix[i])))
            if precisions[i] ==0 and recalls[i] ==0:
                f1s.append(0)
            else:
                f1s.append(2*precisions[i]*recalls[i]/(precisions[i]+recalls[i]))
        self.print_macro_results(accuracy_score(y_test,y_pred), np.mean(precisions), np.mean(recalls), np.mean(f1s))
        for i in range(len(categories)):
            self.print_category_results(categories[i], precisions[i], recalls[i], f1s[i])
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
            rfc = RandomForestClassifier(n_estimators=i, random_state=90)
            score = cross_val_score(rfc, x, y, cv=10).mean()
            if score > max_score:
                max_score = score
                best_n = i

        # print(best_n)
        rfc = RandomForestClassifier(n_estimators=best_n, random_state=90).fit(x, y)
        # Evaluate learned model on testing data, and print the results.
        x_test, y_test = self.loadData("test")
        x_test = pd.get_dummies(x_test)
        miss_columns = set(x) - set(x_test)
        for col in miss_columns:
            x_test[col] = 0
        y_pred = rfc.predict(x_test)
        matrix = confusion_matrix(y_test,y_pred)
        categories = ["teacher", "health", "service", "at_home", "other"]
        # print(matrix)
        precisions = []
        recalls = []
        f1s = []
        for i in range(len(categories)):
            precisions.append(matrix[i][i] / (sum(matrix[:, i])))
            recalls.append(matrix[i][i] / (sum(matrix[i])))
            if precisions[i] == 0 and recalls[i] == 0:
                f1s.append(0)
            else:
                f1s.append(2 * precisions[i] * recalls[i] / (precisions[i] + recalls[i]))
        self.print_macro_results(accuracy_score(y_test, y_pred), np.mean(precisions), np.mean(recalls), np.mean(f1s))
        for i in range(len(categories)):
            self.print_category_results(categories[i], precisions[i], recalls[i], f1s[i])
        return

    def loadData(selfs, type):
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
        x = data.drop(["mjob"],axis=1)
        y = data[["mjob"]]
        return x, y
