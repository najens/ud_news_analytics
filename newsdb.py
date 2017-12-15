import psycopg2

DBNAME = "news"


def get_articles():
    """Return the 3 most popular articles of all time"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(
        """
        SELECT articles.title, subq.views
            FROM articles,
                (SELECT path, count(*) AS views
                    FROM log
                    GROUP BY path
                    ORDER BY views DESC
                    LIMIT 10) AS subq
            WHERE '/article/' || articles.slug = subq.path
            ORDER BY subq.views DESC
            LIMIT 3;
        """
    )
    return c.fetchall()
    db.close


def get_authors():
    """
    Return a list of the most popular authors by total or article page views
    """
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(
        """
        SELECT authors.name, SUM(subq.views) AS total
            FROM articles,
                authors,
                (SELECT path, count(*) AS views
                    FROM log
                    GROUP BY path
                    ) AS subq
            WHERE '/article/' || articles.slug = subq.path
            AND articles.author = authors.id
            GROUP BY authors.name
            ORDER BY total DESC;
        """
    )
    return c.fetchall()
    db.close


def get_errors():
    """Return the days on which > 1 pct of all page requests led to errors"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(
        """
        SELECT errors.day, ((cast(errors.num AS DECIMAL) /
                             cast(total.num AS DECIMAL)) * 100) AS pct
            FROM
                (SELECT date(time) AS day, count(*) AS num
                    FROM log
                    WHERE status = '404 NOT FOUND'
                    GROUP BY day) AS errors,
                (SELECT date(time) AS day, count(*) AS num
                    FROM log
                    GROUP BY day) AS total
            WHERE errors.day = total.day
            AND (((cast(errors.num AS DECIMAL) /
                   cast(total.num AS DECIMAL)) * 100) > 1)
            ORDER BY pct DESC;
        """
    )
    return c.fetchall()
    db.close
