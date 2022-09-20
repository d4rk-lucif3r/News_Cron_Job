import os
from manager.news import get_news
from sqlalchemy import create_engine

ssl_args = {'ssl_ca':  'assets/cacert.pem'}

host = os.getenv('HOST')
username = os.getenv('DB_USER')
password = os.getenv('PASSWORD')
db = os.getenv('DATABASE')

engine = create_engine('mysql+pymysql://{}:{}@{}/{}'.format(
    username, password, host, db
    ), connect_args=ssl_args)

if __name__ == '__main__':
    print("Getting news")
    get_news(engine)
    