from sklearn import svm
from data_processing4 import data_extraction
import numpy as np

"""

Need to classify every trading days as either up or down.
I will give every day that closed above the open price a 1.
Otherwise, the day will be classified with a 0.

"""




x_train, y_train, x_test, y_test = data_extraction('TQQQ.csv')
#y_train = np.reshape(y_train, (-1,1))
x_test = np.reshape(x_test, (1,-1))
y_test = np.reshape(y_test, (1,-1))


# Classification
clf = svm.SVC(kernel='rbf', C=1e3, gamma=0.05)
clf.fit(x_train, y_train)
prediction = clf.predict(x_test)

print('Prediction: {}'.format(prediction))
print('Actual: {}'.format(y_test))
print('Score: {}'.format(clf.score(x_test, y_test)))