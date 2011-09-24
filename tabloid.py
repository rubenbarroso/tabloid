from ConfigParser import ConfigParser
from os import listdir
from os.path import join
import re
from paginator import Paginator
from post import Post

post_pattern = re.compile('^\d{4}_\d{2}_\d{2}_\d{2}_\d{2}$')

class Tabloid:
    """
    """

    def __init__(self):
        self.metadata = self._read_tabloid_metadata()

    def _read_tabloid_metadata(self):
        """Reloads the metadata from tabloid.config"""

        config = ConfigParser()
        config.read("contents/tabloid.config")

        metadata = {}

        for section in config.sections():
            for name, value in config.items(section):
                metadata[name] = value
        return metadata

    def load(self):
        def _list_post_locations():
            """
            """

            def is_post(dir):
                return not post_pattern.match(dir) is None

            dirs = listdir('contents/posts')
            return sorted([join('contents/posts', dir) for dir in dirs if is_post(dir)], reverse=True)

        self.post_locations = _list_post_locations()

    def get_paginator(self):
        page_size = int(self.metadata['page_size'])

        def _generate(post_location):
            return Post(post_location)

        return Paginator(self.post_locations, page_size, _generate)

    def title(self):
        return self.metadata['title']

    def author(self):
        return self.metadata['author']
