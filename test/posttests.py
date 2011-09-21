import unittest
from post import PostMetadata, Post

class PostTestCase(unittest.TestCase):
    def test_simple_render(self):
        """Check simple post rendering capabilities"""
        metadata = PostMetadata("My test post")
        post = Post(metadata, "Post contents here.")
        self.assertEqual(post.render(), "Post contents here.")

if __name__ == '__main__':
    unittest.main()
