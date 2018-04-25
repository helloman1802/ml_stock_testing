from sklearn.linear_model import SGDClassifier
from data_processing2 import data_extraction
import numpy as np

x_train, y_train, x_test, y_test = data_extraction('GOOG.csv')

y_train = np.reshape(y_train, (-1,1))
y_test = np.reshape(y_test, (-1,1))
print('Data used to predict: {}'.format(x_test))
print('Data to compare predition with: {}'.format(y_test))
#print(np.shape(x_train))
#print(np.shape(y_train))
clf = SGDClassifier(loss='hinge', penalty='l2')
clf.fit(x_train, y_train)
print(clf.predict(x_test))