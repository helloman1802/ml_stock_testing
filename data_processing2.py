import pandas as pd
import numpy as np

def data_extraction(csv):
    df = pd.read_csv(csv)
    df = df[['Open', 'Volume', 'Up or Down']]
    t = 0
    for key, value in df.iterrows():
        if t == 0:
            t +=1
            df['Up or Down'].iloc[key] = 0
        else:
            if df['Open'].iloc[key] - df['Open'].iloc[key-1] > 0:
                df['Up or Down'].iloc[key] = 1
            else:
                df['Up or Down'].iloc[key] = 0
    
    df['Up or Down'] = df['Up or Down'].astype(int)
    df['Volume'] = df['Volume'].astype(int)

    x = df[['Open','Volume']]
    y = df['Up or Down']
    x_np = x.as_matrix()
    y_np = y.as_matrix()
    x_train = x_np[3300:3419]
    y_train = y_np[3300:3419]
    x_test = x_np[-1:]
    y_test = y_np[-1:]
    return x_train, y_train, x_test, y_test
    
data_extraction('GOOG.csv')