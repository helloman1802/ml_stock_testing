from keras.models import Sequential
from keras.layers import LSTM, Dense, Activation, Dropout
import numpy as np
import time
import data_processing2

x_train, y_train, x_test, y_test = data_processing2.data_extraction('GOOG.csv')

model = Sequential()
model.add(Dense(50, activation='relu', input_dim=4))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=150, batch_size=100)
scores = model.evaluate(x_test, y_test)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))