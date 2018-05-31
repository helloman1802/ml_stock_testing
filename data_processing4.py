import pandas as pd
import numpy as np

def data_extraction(csv):
    days = 15
    sma1 = 200 + days


    df = pd.read_csv(csv)
    df = df[['Open', 'Close', 'High', 'Low', 'Volume']]
    up_down = []

    print(df)
    """
    for key, row in df.iterrows():
        if key == 0:
            up_down.append(0)
        else:
            print(row['Close']-df.loc[df['Open']])
    """
    #print(up_down)

    """
    open_list = []
    close_list = []
    volume_list = []
    high_list = []
    low_list = []

    # For every day, get the SMA for each feature.
    for i in range(len(df)):
        open_sma1 = 0
        close_sma1 = 0
        volume_sma1 = 0
        high_sma1 = 0
        low_sma1 = 0
        for f in range(sma1):
            open_sma1 += df.iloc[f+i]['Open']
            close_sma1 += df.iloc[f+i]['Close']
            volume_sma1 += df.iloc[f+i]['Volume']
            high_sma1 += df.iloc[f+i]['High']
            low_sma1 += df.iloc[f+i]['Low']
            
        
        open_list.append(open_sma1/sma1)
        close_list.append(close_sma1/sma1)
        volume_list.append(volume_sma1/sma1)
        high_list.append(high_sma1/sma1)
        low_list.append(low_sma1/sma1)
            
    open_frame = pd.Series(open_list)
    close_frame = pd.Series(close_list)
    volume_frame = pd.Series(volume_list)
    high_frame = pd.Series(high_list)
    low_frame = pd.Series(low_list)


    frames = [df, open_frame, close_frame, volume_frame, high_frame, low_frame]
    df = pd.concat(frames, axis=1)
    
    





    x = df[['Low', 'High', 'Open', 'Volume', 0, 1, 2, 3, 4]]
    y = df['Close']
    x_np = x.as_matrix()
    y_np = y.as_matrix()
    x_train = x_np[:days-1]
    y_train = y_np[:days-1]
    x_test = x_np[-1]
    y_test = y_np[-1]
    return x_train, y_train, x_test, y_test
    """    
data_extraction('TQQQ.csv')