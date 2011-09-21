import unittest
from renderer import HeaderRenderer, Renderer, ParagraphRenderer

class RendererTestCase(unittest.TestCase):
    """ """

    def setUp(self):
        self.cases = [('# Title 1\n',
                       '<h1>Title 1</h1>\n'),
            ('# Title\n\nParagraph\n',
             '<h1>Title</h1>\n<p>Paragraph</p>\n')]

    def test_render(self):
        """ """
        renderer = Renderer()
        for input, output in self.cases:
            result = renderer.render(input)
            self.assertEqual(result, output)


class ParagraphRendererTestCase(unittest.TestCase):
    """ """

    def setUp(self):
        self.cases = [('\n\nThis is a paragraph\n',
                       '\n<p>This is a paragraph</p>\n'),
            ('\n\nThis is a\tparagraph\n',
             '\n<p>This is a\tparagraph</p>\n'),
            ('\n\nThis is a\nparagraph\n',
             '\n<p>This is a\nparagraph</p>\n')]

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
            (' ## Title 2', ' ## Title 2')]

    def test_ignored(self):
        renderer = HeaderRenderer()
        for input, output in self.cases:
            result = renderer.render(input)
            self.assertEqual(output, result)

if __name__ == '__main__':
    unittest.main()