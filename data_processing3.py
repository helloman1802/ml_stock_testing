import pandas as pd
import numpy as np

def data_extraction(csv):
    days = 15
    df = pd.read_csv(csv)
    df = df[['Open', 'Volume', 'Close', 'High', 'Low']]
    df = df.head(days)
    
    
    
    
    df['Volume'] = df['Volume'].astype(int)

    x = df[['Low', 'High', 'Open', 'Volume']]
    y = df['Close']
    x_np = x.as_matrix()
    y_np = y.as_matrix()
    x_train = x_np[:days-1]
    y_train = y_np[:days-1]
    x_test = x_np[-days-1:]
    y_test = y_np[-days-1:]
    return x_train, y_train, x_test, y_test
    
data_extraction('GOOG.csv')