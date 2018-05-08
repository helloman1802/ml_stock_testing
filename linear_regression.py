from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import cross_val_predict
from sklearn import linear_model
import matplotlib.pyplot as plt
import pandas as pd
from data_processing3 import data_extraction
import numpy as np


lr = linear_model.LinearRegression()

x_train, y_train, x_test, y_test = data_extraction('GOOG.csv')


y_train = np.reshape(y_train, (-1,1))
y_test = np.reshape(y_test, (-1,1))
x_train = np.reshape(x_train, (-1,1))
x_test = np.reshape(x_test, (-1,1))

lr.fit(x_train, y_train)

prediction = lr.predict(x_test)

df = pd.DataFrame(prediction)
df2 = pd.DataFrame(y_test)
frames = [df, df2]
df = pd.concat(frames, axis=1)
df.columns = ['Prediction', 'Actual']
df.to_csv('predition_comparison.csv')
print(df)

print('Mean square error: {}'.format(mean_squared_error(y_test, prediction)))
print('Variance Score: {}'.format(r2_score(y_test, prediction)))

plt.scatter(x_test, y_test, color='black')
plt.plot(x_test, prediction, color='blue', linewidth=3)
plt.xticks(())
plt.yticks(())
plt.show()