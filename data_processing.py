import pandas as pd
import numpy as np
 
"""
I am going to get 31 days of data in a row.
The first 30 days will be input data and the
final day will be the output.

That means the shape of my input data should look like:

[number_of_data_points, 30, number_of_classes]

The shape of my output data should look like:

[number_of_30_day_arrays, number_of_classes]
"""



def data_extraction(csv):
    df = pd.read_csv(csv)
    df = df.drop(['Date','Close'], axis=1)
    extracted_data = df.as_matrix()
    

    
    x_data = []
    y_data = []
    t = 0

    for day in extracted_data:
        x_data.append(day[np.arange(len(day))!=3])
        y_data.append(day[3])
    


    x_train = np.array(x_data[:-10])
    y_train = np.array(y_data[:-10])
    
    x_test = np.array(x_data[-10:])
    y_test = np.array(y_data[-10:])

    print(np.shape(x_train))
    return x_train, y_train, x_test, y_test


    
def test_data_extraction(csv):
    df = pd.read_csv(csv)
    df = df.drop(['Date','Open','High','Low','Close'], axis=1)
    extracted_data = df.as_matrix()

    t = 0
    nut_bucket = []
    for day in extracted_data:
        t += 1
        if t != 16:
            nut_bucket.append(day)
        else:
            break
    
    nut_bucket = np.array(nut_bucket)
    print(np.shape(nut_bucket))
    return nut_bucket

data_extraction('GOOG.csv')