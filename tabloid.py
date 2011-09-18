from ConfigParser import ConfigParser

class Tabloid:
    """
    """

    def __init__(self, metadata):
        self.metadata = metadata


class TabloidMetadata:
    """
    """

    def __init__(self, metadata):
        self.title = metadata['title']
        self.tagline = metadata['tagline']
        self.author = metadata['author']
        self.page_size = metadata['page_size']


def read_tabloid_metadata():
    """ Reloads the metadata from tabloid.config
    """
    config = ConfigParser()
    config.read("contents/tabloid.config")
    title = config.get("blog", "title")
    tagline = config.get("blog", "tagline")
    author = config.get("blog", "author")
    page_size = config.get("blog", "page_size")
    return TabloidMetadata({'title': title,
                            'tagline': tagline,
                            'author': author,
                            'page_size': page_size})
