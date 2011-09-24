from __future__ import with_statement
from ConfigParser import ConfigParser
from renderer import Renderer
from os.path import join

class Post:
    """ Metadata and contents of a post.
    """

    def __init__(self, location):
        self.metadata = self._read_post_metadata(location)
        self.content = self._read_post_content(location)

    def _read_post_metadata(self, post_location):
        """ Reads the metadata of a post from a file."""
        config = ConfigParser()
        config.read(join(post_location, "post.config"))
        title = config.get("post", "title")
        return PostMetadata(title)

    def _read_post_content(self, post_location):
        """ Reads the contents of a post from a file."""
        post_content_filename = join(post_location, "post.tabloid")
        with open(post_content_filename) as content_file:
            return content_file.read()

    def render(self):
        """ Renders the contents of this post to be viewed in the browser."""
        return Renderer().render(self.content)


class PostMetadata:
    """ Metadata of a post.

        This class encapsulated the metadata associated to a post.
        Useful when we extend it with more information so that we
        do not need to change all the instantiations of Post.

        title - the title of the post - a string
    """

    def __init__(self, title):
        self.title = title


    
