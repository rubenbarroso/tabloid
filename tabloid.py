from ConfigParser import ConfigParser
from os import listdir
import re
from sets import Set
from paginator import Paginator
from post import Post

post_timestamp_pattern = re.compile('^\d{4}_\d{2}_\d{2}_\d{2}_\d{2}$')

class Tabloid:
    """ """

    def __init__(self):
        self.metadata = self._read_tabloid_metadata()
        self.posts = self._load_posts()

    def _read_tabloid_metadata(self):
        """Reloads the metadata from tabloid.config"""

        config = ConfigParser()
        config.read("contents/tabloid.config")

        metadata = {}

        for section in config.sections():
            for name, value in config.items(section):
                metadata[name] = value
        return metadata

    def _load_posts(self):
        def _is_post(dir):
            return not post_timestamp_pattern.match(dir) is None

        posts = [Post(dir) for dir in listdir('contents/posts') if _is_post(dir)]
        return sorted(posts, key=lambda post: post.metadata.timestamp, reverse=True)

    def get_paginator(self, filters=None):
        if not filters: filters = []

        def _apply_filters(post):
            for filter in filters:
                if not filter(post):
                    return False
            return True

        filtered_posts = [post for post in self.posts if _apply_filters(post)]
        return Paginator(filtered_posts, self.page_size())

    def get_all_categories(self):
        categories = Set(['no_category'])
        for post in self.posts:
            [categories.add(category) for category in post.metadata.categories]
        return categories

    def title(self):
        return self.metadata['title']

    def author(self):
        return self.metadata['author']

    def page_size(self):
        return int(self.metadata['page_size'])
