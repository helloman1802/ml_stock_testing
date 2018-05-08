from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score
from data_processing2 import data_extraction
import numpy as np

x_train, y_train, x_test, y_test = data_extraction('GOOG.csv')

y_train = np.reshape(y_train, (-1,1))
y_test = np.reshape(y_test, (-1,1))
print('Finished processing data')
print('Data used to predict: {}'.format(x_test))
print('Data to compare predition with: {}'.format(y_test))
#print(np.shape(x_train))
#print(np.shape(y_train))
clf = linear_model.LinearRegression()
clf.fit(x_train, y_train)
prediction = clf.predict(x_test)
print('prediction: {}'.format(prediction))