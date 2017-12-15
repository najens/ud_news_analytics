# ud_news_analytics

ud_news_analytics is a simple python flask app that returns analytics using queries from a news website database. The results are printed on the server's main page.

## Software Requirements

- [Python 3.6.x](https://www.python.org/downloads/release/python-2714/)
- [PostgreSQL 9.5+](https://www.postgresql.org/download/)
- [Git or Git Bash](https://git-scm.com/downloads)

## Installation Instructions

Open Git or Git Bash in your workspace directory

Clone the GitHub repository
```
$ git clone https://github.com/najens/ud_news_analytics.git
```

Navigate to project folder
```
$ cd ud_news_analytics
```

Create a virtual environment
```
$ python3 -m venv ./venv
```

Activate virtual environment
```
$ source venv/Scripts/activate
```

Install module dependencies
```
$ pip3 install -r requirements.txt
```

## Create DB

Create empty news database
```
$ createdb news
```

[Download newsdata.zip](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

Extract newsdata.sql into the ud_news_analytics directory

Load tables and data into news database
```
$ psql -d news -f newsdata.sql
```

## Run App

Run the python server
```
$ ./news.py
```

Go to *localhost:5555* in your favorite browser to view query results
