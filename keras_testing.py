from keras.models import Sequential
from keras.layers import Dense
from data_processing2 import data_extraction
import numpy as np
import pandas as pd
x_train, y_train, x_test, y_test = data_extraction('GOOG.csv')
y_train = np.reshape(y_train, (-1,1))
y_test = np.reshape(y_test, (-1,1))
print('Finished processing data')
print('Data used to predict: {}'.format(x_test))
print('Data to compare predition with: {}'.format(y_test))

# split into input (X) and output (Y) variables

# create model
model = Sequential()

model.add(Dense(12, input_dim=2, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# Fit the model
model.fit(x_train, y_train, epochs=150, batch_size=10)
# evaluate the model
scores = model.evaluate(x_test, y_test)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))