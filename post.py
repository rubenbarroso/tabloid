from __future__ import with_statement
from ConfigParser import ConfigParser
from renderer import Renderer
from os.path import join

class Post:
    """ Metadata and contents of a post"""

    def __init__(self, post_location):
        self.post_location = post_location
        self.metadata = self._read_post_metadata(post_location)
        self.content = self._read_post_content(post_location)

    def _read_post_metadata(self, post_location):
        """ Reads the metadata of a post from a file"""
        config = ConfigParser()
        config.read(join(post_location, "post.config"))
        title = config.get("post", "title")
        return PostMetadata(post_location, title)

    def _read_post_content(self, post_location):
        """ Reads the contents of a post from a file"""
        post_content_filename = join(post_location, "post.tabloid")
        with open(post_content_filename) as content_file:
            return content_file.read()

    def render(self):
        """ Renders the contents of this post to be viewed in the browser"""
        output = ['\n', '<h1><a href="?post=%s">%s</a></h1>' %
                        (self.metadata.post_timestamp, self.metadata.title), '\n']
        renderer = Renderer(self.post_location)
        output.append(renderer.render(self.content))
        return ''.join(output)


class PostMetadata:
    """ Metadata of a post.

        This class encapsulated the metadata associated to a post.
        Useful when we extend it with more information so that we
        do not need to change all the instantiations of Post.

        title - the title of the post - a string
    """

    def __init__(self, post_location, title):
        self.post_timestamp = self._get_post_timestamp(post_location)
        self.title = title

    def _get_post_timestamp(self, post_location):
        return post_location.rpartition('/')[2]


    
