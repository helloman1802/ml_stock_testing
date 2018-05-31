from sklearn.naive_bayes import GaussianNB
from data_processing3 import data_extraction
import numpy as np

x_train, y_train, x_test, y_test = data_extraction('TQQQ.csv')
y_train = map(int, [137.02, 137.56, 143.31, 145.39, 145.4 , 146.09, 146.35, 146.43,
       147.51, 147.97, 153.58, 154.94, 156.71, 157.23])
y_train = np.reshape(y_train, (-1,1))
clf = GaussianNB()
clf.fit(x_train, y_train)
print(clf.predict(y_test))
