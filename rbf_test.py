import numpy as np
from sklearn.svm import SVR
from data_processing2 import data_extraction
import matplotlib.pyplot as plt


x_train, y_train, x_test, y_test = data_extraction('GOOG.csv')


svr_rbf = SVR(kernel='rbf',C=1e3,gamma=0.1)
svr_rbf.fit(x_train, y_train)
plt.plot(svr_rbf.predict(x_test))
plt.show()