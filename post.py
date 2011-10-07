from __future__ import with_statement
from ConfigParser import ConfigParser
import os
import pickle
from renderer import Renderer
from os.path import join

class Post:
    """Metadata and contents of a post"""

    def __init__(self, timestamp):
        self.metadata = self._read_post_metadata(timestamp)

    def _read_post_metadata(self, timestamp):
        """Reads the metadata of a post from a config file"""
        location = join('contents/posts', timestamp)

        config = ConfigParser()
        config.read(join(location, "post.config"))
        title = config.get("post", "title")
        categories = config.get("post", "category").split(',')
        return PostMetadata(timestamp, location, title, categories)

    def read_content(self):
        """Reads the contents of a post from a file or cache"""
        cached_contents_pathname = join(self.metadata.location, ".cached_contents")
        if os.path.exists(cached_contents_pathname):
            with open(cached_contents_pathname) as cached_contents:
                return pickle.load(cached_contents)
        else:
            post_content_pathname = join(self.metadata.location, "post.tabloid")
            with open(post_content_pathname) as content_file:
                contents = content_file.read()
            return contents

    def render(self):
        """Renders the contents of this post to be viewed in the browser"""
        # title
        output = ['\n', '<h1><a href="?post=%s">%s</a></h1>' %
                        (self.metadata.timestamp, self.metadata.title), '\n']

        # content
        renderer = Renderer(self.metadata.location)
        content = self.read_content()
        output.append(renderer.render(content))

        # categories
        output.append('<p><small>Posted on ')
        [output.append('<a href="?category=%s">%s</a> ' % (category, category)) for category in
         self.metadata.categories]
        output.append('</small></p>')
        return ''.join(output)


class PostMetadata:
    """ Metadata of a post.

        This class encapsulated the metadata associated to a post.
        Useful when we extend it with more information so that we
        do not need to change all the instantiations of Post.

        title - the title of the post - a string
    """

    def __init__(self, timestamp, location, title, categories):
        self.timestamp = timestamp
        self.location = location
        self.title = title
        self.categories = sorted([category.strip() for category in categories])


def with_timestamp(timestamp=None):
    def _pred(post):
        if timestamp is None:
            return True
        else:
            return post.metadata.timestamp == timestamp

    return _pred


def with_category(category=None):
    def _pred(post):
        if category is None:
            return True
        else:
            return category in post.metadata.categories

    return _pred
