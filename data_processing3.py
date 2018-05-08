import pandas as pd
import numpy as np

def data_extraction(csv):
    df = pd.read_csv(csv)
    df = df[['Open', 'Volume', 'Adj Close', 'High', 'Low']]
    df = df.head(30)
    
    
    
    
    df['Volume'] = df['Volume'].astype(int)

    x = df['Low']
    y = df['Adj Close']
    x_np = x.as_matrix()
    y_np = y.as_matrix()
    x_train = x_np[:20]
    y_train = y_np[:20]
    x_test = x_np[-20:]
    y_test = y_np[-20:]
    return x_train, y_train, x_test, y_test
    
data_extraction('GOOG.csv')