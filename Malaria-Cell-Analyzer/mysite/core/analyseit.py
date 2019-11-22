import cv2
import glob
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn import metrics
import joblib
import numpy as np

list = []

class Malaria_Cell_Analyzer:
    dirList = glob.glob("media/*.png")
    for img_path in dirList:
        im = cv2.imread(img_path)
        im = cv2.GaussianBlur(im, (5, 5), 2)
        im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(im_gray, 127, 255, 0)
        contours, _ = cv2.findContours(thresh, 1, 2)

        for contour in contours:
            cv2.drawContours(im_gray, contours, -1, (0, 255, 0), 3)
            cv2.imwrite("media/processed.png", im_gray)
            #cv2.imshow("window2", im_gray)
            #cv2.waitKey(10000)

        for i in range(5):
            try:
                area = cv2.contourArea(contours[i])
                list.append(area)
            except:
                list.append(0)
        print(list)
        cv2.waitKey(2000)
        #os.remove(img_path)


##Step1: Load Dataset

dataframe = pd.read_csv("cell_images/dataset.csv")
#print(dataframe.head(10))

#Step2: Split into training and test data
x = dataframe.drop(["Label"],axis=1)
y = dataframe["Label"]
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)

##Step4: Build models

##@-Model 1. RandomForest
#model = RandomForestClassifier(n_estimators=100, max_depth=5)
clf=RandomForestClassifier(n_estimators=200, bootstrap=False,
class_weight=None, criterion='entropy', max_features='auto', max_leaf_nodes=None, min_impurity_decrease=0.0, min_impurity_split=None, min_weight_fraction_leaf=0.0, n_jobs=6, oob_score=False, random_state=np.random.seed(999), verbose=0, warm_start=False)

clf.fit(x_train, y_train)
#model.fit(x_train, y_train)
joblib.dump(clf, "rf_malaria_100_5")

##Step5: Make predictions and get classification report

predictions = clf.predict(x_test)

print(metrics.classification_report(predictions, y_test))
print("Accuracy is :", clf.score(x_test, y_test))

Xnew = [list]

y_prednew = clf.predict(Xnew)
print("The cell is :", y_prednew)

