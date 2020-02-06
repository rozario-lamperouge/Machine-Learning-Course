import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv('wo_men1.csv')
df.dropna(inplace =True)

df = np.array(df)
X = df[:,2:]
Y = df[:,1]

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2)

clf = KNeighborsClassifier()
clf.fit(X_train,Y_train)

score = clf.score(X_train,Y_train)
print(clf.predict([[175,44]]))

predict = clf.predict(X_test)
print(accuracy_score(Y_test, predict))
