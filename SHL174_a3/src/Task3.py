import pandas as pd
from sklearn.model_selection import cross_val_score
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import sklearn.metrics as metrics
from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.metrics import hamming_loss
from sklearn.svm import LinearSVC
import warnings
warnings.filterwarnings('ignore')


class Task3:
    # please feel free to create new python files, adding functions and attributes to do training, validation, testing

    def __init__(self):
        print("================Task 3================")
        return
    # SVM model
    def model_1_run(self):
        print("Model 1:")
        # Train the model 1 with your best hyper parameters (if have) and features on training data.
        x,y = self.loadData("train")
        x =pd.get_dummies(x)
        clf1 = OneVsRestClassifier(SVC(kernel='linear'), n_jobs=-1)
        clf1.fit(x,y)
        OneVsRestClassifier(
            estimator=SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, decision_function_shape=None, degree=3,
                          gamma='auto', kernel='linear', max_iter=-1, probability=False, random_state=None,
                          shrinking=True, tol=0.001, verbose=False), n_jobs=-1)

        # Evaluate learned model on testing data, and print the results.
        x_test, y_test = self.loadData("test")
        x_test = pd.get_dummies(x_test)
        miss_columns = set(x) - set(x_test)
        for col in miss_columns:
            x_test[col] = 0
        y_pred = clf1.predict(x_test)

        print("Accuracy\t" + str(accuracy_score(y_test,y_pred)) + "\tHamming loss\t" + str(hamming_loss(y_test,y_pred)))
        return

    # decision tree model
    def model_2_run(self):
        print("--------------------\nModel 2:")
        # Train the model 2 with your best hyper parameters (if have) and features on training data.
        x, y = self.loadData("train")
        x = pd.get_dummies(x)
        clf1 = OneVsRestClassifier(RandomForestClassifier(n_estimators=180, random_state=90), n_jobs=-1)
        clf1.fit(x, y)
        OneVsRestClassifier(
            estimator=RandomForestClassifier(n_estimators=180, random_state=90), n_jobs=-1)

        # Evaluate learned model on testing data, and print the results.
        x_test, y_test = self.loadData("test")
        x_test = pd.get_dummies(x_test)
        miss_columns = set(x) - set(x_test)
        for col in miss_columns:
            x_test[col] = 0
        y_pred = clf1.predict(x_test)

        print(
            "Accuracy\t" + str(accuracy_score(y_test, y_pred)) + "\tHamming loss\t" + str(hamming_loss(y_test, y_pred)))
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

        y = data[["edusupport"]]
        new_y = pd.DataFrame(columns=["edu_family", "edu_school", "edu_paid", "edu_no"])
        for index,row in y.iterrows():
            one_row = dict()
            if "family" in row["edusupport"]:
                one_row["edu_family"] = 1
            else:
                one_row["edu_family"] = 0
            if "school" in row["edusupport"]:
                one_row["edu_school"] = 1
            else:
                one_row["edu_school"] = 0
            if "paid" in row["edusupport"]:
                one_row["edu_paid"] = 1
            else:
                one_row["edu_paid"] = 0
            if "no" in row["edusupport"]:
                one_row["edu_no"] = 1
            else:
                one_row["edu_no"] = 0
            new_y = new_y.append(one_row,ignore_index=True)

        new_y = new_y.astype('int')
        data = data.drop(["edusupport"],axis=1)
        new_data = pd.concat([data,new_y],axis=1)
        x = new_data.drop(["edu_family", "edu_school", "edu_paid", "edu_no"],axis=1)
        y = new_data[["edu_family", "edu_school", "edu_paid", "edu_no"]]
        return x, y