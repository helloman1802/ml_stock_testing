from newsapi.sources import Sources
from newsapi.articles import Articles
from textblob import TextBlob




api_key = "1db5bfc5325a40e28fdf172b49198ce7"
def daily_sentiment():
    s = Sources(API_KEY=api_key)
    sources = s.get(category='business', language='en', country='us')
    sources = sources['sources']
    source_list = []
    for i in sources:
        source_list.append(i['id'])

    a = Articles(API_KEY=api_key)
    article_list = []

    for source in source_list:
        articles = a.get(source)
        for article in articles['articles']:
            article_list.append(article['description'])

    total_polarity = 0
    for article in article_list:
        analysis = TextBlob(article)
        # set sentiment
        if analysis.sentiment.polarity > 0:
            #print('Polarity: {} \n Article: {}'.format(analysis.sentiment.polarity, article))
            total_polarity += analysis.sentiment.polarity
        elif analysis.sentiment.polarity < 0:
            #print('Polarity: {} \n Article: {}'.format(analysis.sentiment.polarity, article))
            total_polarity += analysis.sentiment.polarity

    return total_polarity

