from collections import namedtuple
from systemd import journal

Article = namedtuple('Article', 'title, content, tags')

class Blog(object):
    """An interface to interact with the blog"""

    def send(self, article):
        """Write an article to the blog"""
        journal.send(article.content,
            ARTICLE_TITLE=article.title,
            ARTICLE_TAGS=', '.join(article.tags),
            SYSLOG_IDENTIFIER='systemd-blog')
