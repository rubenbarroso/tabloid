import unittest
from renderer import HeaderRenderer, Renderer, ParagraphRenderer, EmphasisRenderer, ImageRenderer, LinkRenderer, CodeRenderer

class RendererTestCase(unittest.TestCase):
    """ """

    def setUp(self):
        self.cases = [('# Title 1\n',
                       '<h1>Title 1</h1>\n'),
            ('# Title\n\nParagraph\n\n',
             '<h1>Title</h1>\n\n<p>Paragraph</p>\n\n'),
            ('## Post Example\n\nThis is my first post, yay!\n\n',
             '<h2>Post Example</h2>\n\n<p>This is my first post, yay!</p>\n\n')]

    def test_render(self):
        """ """
        renderer = Renderer('contents/post/2009_08_05_12_56')
        for input, output in self.cases:
            result = renderer.render(input)
            self.assertEqual(result, output)


class ParagraphRendererTestCase(unittest.TestCase):
    """ """

    def setUp(self):
        self.cases = [('\n\nThis is a paragraph\n\n',
                       '<p>This is a paragraph</p>\n\n'),
            ('This is a\tparagraph\n\n',
             '<p>This is a\tparagraph</p>\n\n'),
            ('This is a\nparagraph\n\n',
             '<p>This is a\nparagraph</p>\n\n'),
            ('pre\n\nParagraph\n\n',
             '<p>pre</p>\n\n<p>Paragraph</p>\n\n'),
            ('With a,comma!\n\n\n',
             '<p>With a,comma!</p>\n\n'),
            ('\n\n\nParagraph\n\n',
             '<p>Paragraph</p>\n\n'),
            ('\n\nFirst Paragraph\n\nSecond Paragraph\n\n',
             '<p>First Paragraph</p>\n\n<p>Second Paragraph</p>\n\n')]

    def test_render(self):
        """Verify header rendering"""
        #TODO too much repeated code here
        renderer = ParagraphRenderer()
        for input, output in self.cases:
            result = renderer.render(input)
            self.assertEqual(output, result)


class HeaderRendererTestCase(unittest.TestCase):
    """ """

    def setUp(self):
        self.cases = [('# Title 1\n', '<h1>Title 1</h1>\n'),
            ('## Title 2\n', '<h2>Title 2</h2>\n'),
            ('### Title 3\n', '<h3>Title 3</h3>\n'),
            ('#### Title 4\n', '<h4>Title 4</h4>\n'),
            ('##### Title 5\n', '<h5>Title 5</h5>\n'),
            ('###### Title 6\n', '<h6>Title 6</h6>\n')]

    def test_render(self):
        """Verify header rendering"""
        renderer = HeaderRenderer()
        for input, output in self.cases:
            result = renderer.render(input)
            self.assertEqual(output, result)


class HeaderRendererIgnoreInputTestCase(unittest.TestCase):
    """Verify that string not matching the regexp are left as is"""

    def setUp(self):
        self.cases = [('#Title', '#Title'),
            ('####### Title 7', '####### Title 7'),
            (' ## Title 2', ' ## Title 2'),
            ('##  Title 2', '##  Title 2')]

    def test_ignored(self):
        renderer = HeaderRenderer()
        for input, output in self.cases:
            result = renderer.render(input)
            self.assertEqual(output, result)


class EmphasisRendererTestCase(unittest.TestCase):
    """ """

    def setUp(self):
        self.cases = [('*Emphasized* ', '<em>Emphasized</em> '),
            ('_Emphasized_ ', '<em>Emphasized</em> '),
            ('*Emphasized_ ', '*Emphasized_ '),
            ('_Emphasized* ', '_Emphasized* '),
            ('*Empha\nsized* ', '<em>Empha\nsized</em> '),
            ('2011_09_15_15_50', '2011_09_15_15_50'),
            (' _Gregor Samsa_ ', ' <em>Gregor Samsa</em> '),
            ('_post_,', '<em>post</em>,')]

    def test_render(self):
        """Verify emphasis rendering"""
        renderer = EmphasisRenderer()
        for input, output in self.cases:
            result = renderer.render(input)
            self.assertEqual(output, result)


class ImageRendererTestCase(unittest.TestCase):
    """ """

    def setUp(self):
        self.cases = [('![alt text](img.jpg "title")',
                       '<img src="/path/images/img.jpg" alt="alt text" title="title" />')]

    def test_render(self):
        """Verify image rendering"""
        renderer = ImageRenderer("/path")
        for input, output in self.cases:
            result = renderer.render(input)
            self.assertEqual(output, result)


class LinkRendererTestCase(unittest.TestCase):
    """ """

    def setUp(self):
        self.cases = [('[example link](http://example.com/)',
                       '<a href="http://example.com/">example link</a>'),
            ('[go to oldest post](2011_09_16_15_50)',
             '<a href="?post=2011_09_16_15_50">go to oldest post</a>')]

    def test_render(self):
        """Verify header rendering"""

        renderer = LinkRenderer()
        for input, output in self.cases:
            result = renderer.render(input)
            self.assertEqual(output, result)


class CodeRendererTestCase(unittest.TestCase):
    """ """

    def setUp(self):
        self.cases = [('`int x = 3;`', '<code>int x = 3;</code>'),
            ('`\n x = 3;\n print \'Hello, dude! x =\', x\n`',
             '<code>\n x = 3;\n print \'Hello, dude! x =\', x\n</code>')]

    def test_render(self):
        """Verify code rendering"""

        renderer = CodeRenderer()
        for input, output in self.cases:
            result = renderer.render(input)
            self.assertEqual(output, result)

if __name__ == '__main__':
    unittest.main()