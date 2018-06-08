import requests
from bs4 import BeautifulSoup
import pandas as pd

def web_scrape():
    quote_pages = ['https://finance.yahoo.com/quote/TQQQ?p=TQQQ']
    table_classes = ['W(100%)']
    data = []
    for quote_page, table_class in zip(quote_pages, table_classes):
        
        page = requests.get(quote_page)
        soup = BeautifulSoup(page.content, 'html.parser')
        
        tables = soup.find_all('table', attrs={'class':table_class})
        for table in tables:
            table_body = table.find('tbody')

            rows = table_body.find_all('tr')
            for row in rows:
                cols = row.find_all('td')
                cols = [ele.text.strip() for ele in cols]
                data.append([ele for ele in cols if ele]) 
    stats_df = pd.DataFrame(data)
    stats_df.columns = stats_df.iloc[0]
    stats_df = stats_df.reindex(stats_df.index.drop(0))
    stats_df = stats_df.set_index('Previous Close').T
    stats_df = stats_df.drop(columns=['Bid', 'Ask', 'PE Ratio (TTM)', 'Yield', 'Inception Date'])
    stats_df = stats_df.reset_index()
    stats_df.columns = ['Previous Close', 'Open', 'Day Range', '52 Week Range', 'Volume', 'Avg. Volume', 'Net Assets', 'NAV', 'YTD Return', 'Beta (3y)', 'Expense Ratio (net)']

    return stats_df

