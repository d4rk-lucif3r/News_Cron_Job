# News Cron Job

This is a simple cron job that will check fetch the latest news from the [News API](https://newsapi.org/) and save it to Database.

## Installation

1. Clone the repository
2. Run `pip install -r requirements.txt` to install the dependencies
3. Create a `.env` file and add the following environment variables:
    - `NEWS_API_KEY`: Your NewsAPI API key
    - `HOST`: The host of your database
    - `DATABASE`: The name of your database
    - `DB_USER`: The username of your database
    - `PASSWORD`: The password of your database
4. Run `python main.py` to run the script

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

- [News API](https://newsapi.org/)
- [Python](https://www.python.org/)
