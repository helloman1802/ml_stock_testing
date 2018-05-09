from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import cross_val_predict
from sklearn import linear_model
import matplotlib.pyplot as plt
import pandas as pd
from data_processing3 import data_extraction
import numpy as np


lr = linear_model.LinearRegression()

x_train, y_train, x_test, y_test = data_extraction('TQQQ.csv')



y_test = np.reshape(y_test, (-1,1))
#x_train = np.reshape(x_train, (-1,1))
#x_test = np.reshape(x_test, (-1,1))

lr.fit(x_train, y_train)
print(np.shape(x_test))
prediction = lr.predict(x_test)
print(np.shape(prediction))
df = pd.DataFrame(prediction)
df2 = pd.DataFrame(y_test)
frames = [df, df2]
df = pd.concat(frames, axis=1)
df.columns = ['Prediction', 'Actual']
df.to_csv('predition_comparison.csv')
#print(df)
varience_score = 'Variance Score: {}'.format(r2_score(y_test, prediction))
print('Mean square error: {}'.format(mean_squared_error(y_test, prediction)))
print('Variance Score: {}'.format(r2_score(y_test, prediction)))


"""
fig = plt.figure()
ax = fig.add_subplot(111)
fig.subplots_adjust(top=0.85)
ax.set_title('Google Stock Prediction', fontsize=14, fontweight='bold')
ax.set_xlabel('Daily Adjusted Close Price', fontweight='bold')
ax.set_ylabel('Daily Low Price', fontweight='bold')
ax.text(0.95, 0.01, varience_score, verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='green', fontsize=15)



plt.scatter(x_test, y_test, color='black')
plt.plot(x_test, prediction, color='blue', linewidth=3)
plt.xticks(np.arange(min(x_test), max(x_test)+1, 1.0), rotation=-45)
plt.yticks(np.arange(min(y_test), max(y_test)+1, 1.0))
plt.show()
"""