#!/usr/bin/env python
from flask import Flask, request
from newsdb import get_articles, get_authors, get_errors
from datetime import date

app = Flask(__name__)

q1 = """\nWhat are the most popular articles of all time?\n
ARTICLE VIEWS
"""
q2 = """\n\nWho are the most popular article authors of all time?\n
AUTHOR VIEWS
"""

q3 = """\n\nOn which days did more than 1 % of requests lead to errors?\n
DAY PERCENT
"""

row = """\
%s %s
"""


@app.route('/', methods=['GET'])
def main():
    '''Show data'''
    a1 = "".join(row % (article, views) for article, views in get_articles())
    a2 = "".join(row % (authors, views) for authors, views in get_authors())
    a3 = "".join(row % (day.__format__("%B %d, %Y"), round(percent, 2)) for
                 day, percent in get_errors())

    return q1 + a1 + q2 + a2 + q3 + a3


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555)
