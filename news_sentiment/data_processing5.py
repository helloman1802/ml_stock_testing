import pandas as pd
import numpy as np
from news_sentiment import daily_sentiment
from datetime import datetime
from web_scraper import web_scrape
import re

high_low_pat = '(\d+\.\d+) - (\d+\.\d+)'


def data_processing(csv):
    now = datetime.now()
    existing_csv = pd.read_csv('{}'.format(csv))
    df = pd.DataFrame()
    scraped_df = web_scrape()
    sentiment = daily_sentiment()

    
    df['date'] = now.strftime('%Y-%m-%d')
    df['previous close'] = scraped_df['Previous Close']
    df['volume'] = scraped_df['Volume']
    df['avg volume'] = scraped_df['Avg. Volume']
    df['open'] = scraped_df['Open']
    
    reg1 = re.search(high_low_pat, str(scraped_df['Day Range']))
    if reg1:
        low = reg1.group(1)
        high = reg1.group(2)
    df['low'] = low
    df['high'] = high 
    reg2 = re.search(high_low_pat, str(scraped_df['52 Week Range']))
    if reg2:
        fifty_two_low = reg2.group(1)
        fifty_two_high = reg2.group(2)
    df['52 week low'] = fifty_two_low
    df['52 week high'] = fifty_two_high
    df['sentiment'] = sentiment
    # 1 is an increase in price and 0 is a decrease
    result = float(df['previous close'])-float(df['open'])
    if result > 0:
        up_down = 1
    else:
        up_down = 0
    df['up_down'] = up_down
    
    
    print(df)
    #df.to_csv(csv, index=False)
    
    
      
data_processing('sentiment_dataset.csv')