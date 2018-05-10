import pandas as pd
import numpy as np

def data_extraction(csv):
    days = 15
    sma1 = 5 + days
    sma2 = 20 + days


    df = pd.read_csv(csv)
    df = df[['Open', 'Close', 'High', 'Low', 'Volume']]
    #df = df.iloc[::-1]
    #df.reset_index(drop=True, inplace=True)

        
    open_list1 = []
    volume_list1 = []
    high_list1 = []
    low_list1 = []
    open_list2 = []
    volume_list2 = []
    high_list2 = []
    low_list2 = []

    # For every day, get the SMA for each feature.
    for i in range(days):
        open_sma1 = 0
        volume_sma1 = 0
        high_sma1 = 0
        low_sma1 = 0
        open_sma2 = 0
        volume_sma2 = 0
        high_sma2 = 0
        low_sma2 = 0
        for f in range(sma1):
            open_sma1 += df.iloc[f+i]['Open']
            volume_sma1 += df.iloc[f+i]['Volume']
            high_sma1 += df.iloc[f+i]['High']
            low_sma1 += df.iloc[f+i]['Low']

        for f in range(sma2):
            open_sma2 += df.iloc[f+i]['Open']
            volume_sma2 += df.iloc[f+i]['Volume']
            high_sma2 += df.iloc[f+i]['High']
            low_sma2 += df.iloc[f+i]['Low']
        
        open_list1.append(open_sma1/sma1)
        volume_list1.append(volume_sma1/sma1)
        high_list1.append(high_sma1/sma1)
        low_list1.append(low_sma1/sma1)
        open_list2.append(open_sma1/sma1)
        volume_list2.append(volume_sma1/sma1)
        high_list2.append(high_sma1/sma1)
        low_list2.append(low_sma1/sma1)
            
    open_frame1 = pd.Series(open_list1)
    volume_frame1 = pd.Series(volume_list1)
    high_frame1 = pd.Series(high_list1)
    low_frame1 = pd.Series(low_list1)
    open_frame2 = pd.Series(open_list2)
    volume_frame2 = pd.Series(volume_list2)
    high_frame2 = pd.Series(high_list2)
    low_frame2 = pd.Series(low_list2)


    frames = [df, open_frame1, volume_frame1, high_frame1, low_frame1, open_frame2, volume_frame2, high_frame2, low_frame2]
    df = pd.concat(frames, axis=1)
    df = df.head(days)
    

    x = df[['Low', 'High', 'Open', 'Volume', 0, 1, 2, 3, 4, 5, 6, 7]]
    y = df['Close']
    x_np = x.as_matrix()
    y_np = y.as_matrix()
    x_train = x_np[:days-1]
    y_train = y_np[:days-1]
    x_test = x_np[-days-1:]
    y_test = y_np[-days-1:]
    return x_train, y_train, x_test, y_test
    
data_extraction('TQQQ.csv')