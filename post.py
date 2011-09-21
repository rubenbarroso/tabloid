from __future__ import with_statement
from ConfigParser import ConfigParser
from renderer import Renderer

class Post:
    """ Metadata and contents of a post.
    """
    def __init__(self, metadata, content):
        """ metadata - this post's metadata - a PostMetadata
            content - contents of this post - a string
        """
        self.metadata = metadata
        self.content = content

    def render(self):
        """ Renders the contents of this post to be viewed in the browser.
        """
        renderer = Renderer()
        return renderer.render(self.content)

class PostMetadata:
    """ Metadata of a post.

        This class encapsulated the metadata associated to a post.
        Useful when we extend it with more information so that we
        do not need to change all the instantiations of Post.

        title - the title of the post - a string
    """
    def __init__(self, title):
        self.title = title

def read_post_content(content_filename):
    """ Reads the contents of a post from a file.
    """
    with open(content_filename) as content_file:
        read_content = content_file.read()
    return read_content

def read_post_metadata(metadata_filename):
    """ Reads the metadata of a post from a file.
    """
    config = ConfigParser()
    config.read(metadata_filename)
    title = config.get("post", "title")
    return PostMetadata(title)


    
