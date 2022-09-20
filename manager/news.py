import json
import time
import tempfile
import requests
import os
from logger import error_log, info_log, warning_log
from manager.notifications import new_notification

tmp_dir = tempfile.gettempdir()


def get_news(engine) -> None:
    """
    This function fetches the weather data from newssapi using
    api key provided in env and stores the data in 
    "news.json" 
    New Notification and info log is created each time new data is fetched
    """
    api_key = str(os.getenv('NEWSAPI_KEY'))
    country = 'in'
    url = 'https://newsapi.org/v2/top-headlines?country={}&apiKey={}' \
        .format(country, api_key)
    new_news = requests.get(url)
    new_news = json.loads(new_news.text)
    with open('./news.json', 'w') as news_file:
        json.dump(new_news, news_file, indent=2)

    for i in range(len(new_news['articles'])):
        news_notification = ({'timestamp':
                              time.strftime('%H:%M:%S'),
                              'type': 'News',
                              'title': new_news
                              ['articles'][i]['title'],
                              'description': new_news['articles'][i]['description']})
        news_log = ({'timestamp': time.strftime('%H:%M:%S'),
                     'type': 'news',
                     'description': 'New news articles'
                     + new_news['articles'][i]['title'],
                     'error': ''})
        new_notification(news_notification, engine)
        info_log(news_log)

    with open('./news.json', 'w') as news_file:
        json.dump(new_news, news_file, indent=2)


