from keras.models import Sequential
from keras.layers import LSTM, Dense
import numpy as np
from data_processing import data_extraction, test_data_extraction

x_train, y_train, x_val, y_val = data_extraction('GOOG.csv')

data_dim = 2
timesteps = 1
num_classes = 4

# expected input data shape: (batch_size, timesteps, data_dim)
model = Sequential()
model.add(LSTM(32, return_sequences=True,
               input_shape=(timesteps, data_dim)))  # returns a sequence of vectors of dimension 32
model.add(LSTM(32, return_sequences=True))  # returns a sequence of vectors of dimension 32
model.add(LSTM(32))  # return a single vector of dimension 32
model.add(Dense(2, activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])


model.fit(x_train, y_train,
          batch_size=64, epochs=5,
          validation_data=(x_val, y_val))

print(model.predict(x_val))