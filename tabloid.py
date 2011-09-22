from ConfigParser import ConfigParser
from os import listdir
from os.path import join
import re
from post import read_post_metadata, read_post_content, Post

post_pattern = re.compile('^\d{4}_\d{2}_\d{2}_\d{2}_\d{2}$')

class Tabloid:
    """
    """

    def __init__(self):
        self.metadata = self.read_tabloid_metadata()

    def read_tabloid_metadata(self):
        """Reloads the metadata from tabloid.config"""

        config = ConfigParser()
        config.read("contents/tabloid.config")

        metadata = {}

        for section in config.sections():
            for name, value in config.items(section):
                metadata[name] = value
        return metadata

    def load(self):
        def list_post_locations():
            """
            """

            def is_post(dir):
                return not post_pattern.match(dir) is None

            dirs = listdir('contents/posts')
            return sorted([join('contents/posts', dir) for dir in dirs if is_post(dir)])

        dirs = list_post_locations()
        self.posts = []

        for i in range(min(len(dirs), int(self.metadata['page_size']))):
            post_metadata = read_post_metadata(join(dirs[i], 'post.config'))
            post_content = read_post_content(join(dirs[i], 'post.tabloid'))
            self.posts.append(Post(post_metadata, post_content))

    def title(self):
        return self.metadata['title']

    def author(self):
        return self.metadata['author']