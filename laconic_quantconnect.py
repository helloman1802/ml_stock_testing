import numpy as np
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import cross_val_predict
from sklearn import linear_model
import pandas as pd
from datetime import timedelta, datetime


class BasicTemplateAlgorithm(QCAlgorithm):
    

    def Initialize(self):
        self.stock_long = 'TQQQ'
        self.stock_short = 'SQQQ'

        self.SetStartDate(2013, 10, 1)  #Set Start Date
        self.SetEndDate(2018, 5, 1)    #Set End Date
        self.SetCash(100000)           #Set Strategy Cash
        
        # Add security to security list
        self.AddEquity(self.stock_long, Resolution.Daily)
        self.AddEquity(self.stock_short, Resolution.Daily)
        
        
        self.Schedule.On(self.DateRules.EveryDay("TQQQ"), self.TimeRules.AfterMarketOpen(self.stock_long, 10), self.EveryDayAfterMarketOpen)
        
        
        
        
    def EveryDayAfterMarketOpen(self):
           
        
        
        # Linear regression model
        lr = linear_model.LinearRegression()
        
        # Get 30 days of warmup data so that the regression algorithm
        # can start with enough data to make a prediction.
        
        days = 15
        sma1 = 5 + days
        
        df = self.History([self.stock_short], timedelta(400))
        df = df.iloc[::-1]
        df.reset_index(drop=True, inplace=True)
        
        open_list = []
        volume_list = []
        high_list = []
        low_list = []
        
        # For every day, get the SMA for each feature.
        for i in range(days):
            open_sma1 = 0
            volume_sma1 = 0
            high_sma1 = 0
            low_sma1 = 0
            for f in range(sma1):
                
                open_sma1 += df.iloc[f+i]['open']
                volume_sma1 += df.iloc[f+i]['volume']
                high_sma1 += df.iloc[f+i]['high']
                low_sma1 += df.iloc[f+i]['low']
            
            open_list.append(open_sma1/sma1)
            volume_list.append(volume_sma1/sma1)
            high_list.append(high_sma1/sma1)
            low_list.append(low_sma1/sma1)
                
        open_frame = pd.Series(open_list)
        volume_frame = pd.Series(volume_list)
        high_frame = pd.Series(high_list)
        low_frame = pd.Series(low_list)
    
    
        frames = [df, open_frame, volume_frame, high_frame, low_frame]
        df = pd.concat(frames, axis=1)
        df = df.head(days)
        
        # Separate x data and y labels
        x = df[['low', 'high', 'open', 'volume', 0, 1, 2, 3]]
        y = df['close']
        # Convert to nunpy arrays
        x_train = x.as_matrix()
        y_train = y.as_matrix()
        
        
        
        # Fit model to training data
        lr.fit(x_train, y_train)
        
        # This is the data that will be used to predict the 
        # current days closing price.
        
        # Current day's paramaters
        today_low = self.Securities[self.stock_short].Low
        today_high = self.Securities[self.stock_short].High
        today_open = self.Securities[self.stock_short].Open
        today_volume = self.Securities[self.stock_short].Volume
        open_sma1 = df.iloc[0]['open']
        volume_sma1 = df.iloc[0]['volume']
        high_sma1 = df.iloc[0]['high']
        low_sma1 = df.iloc[0]['low']
        
            
        
        today_data = [[today_low, today_high, today_open, today_volume, open_sma1, volume_sma1, high_sma1, low_sma1]]
        
        
        
        # Predict closing price given today's low
        prediction = lr.predict(today_data)
        
        
        
        #self.Log('Prediction: {}'.format(prediction))
        #self.Log('Actual: {}'.format(yester_close))
        
        
        percent_change = float(self.Securities[self.stock_long].Price)/prediction[0]
        
        
        
        
        
        
        if percent_change < 0.9:
            if not self.Portfolio.Invested:
                self.Log('{}'.format(datetime.now()))
                self.SetHoldings(self.stock_short, 1)
        elif percent_change > 1.1:
            self.Log('{}'.format(percent_change))
            if self.Portfolio.Invested:
                self.SetHoldings(self.stock_short, 0)
                self.SetHoldings(self.stock_long, 1)
            else:
                self.SetHoldings(self.stock_long, 1)
        else:
            if self.Portfolio.Invested:
                self.SetHoldings(self.stock_long, 0)
                self.SetHoldings(self.stock_short, 0)
        
        
    
            
            
            
                
                
    #def OnData(self, data):