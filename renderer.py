import re

class Renderer:
    """ """

    def __init__(self):
        self.renderers = [ParagraphRenderer(),
                          HeaderRenderer(),
                          EmphasisRenderer()]

    def render(self, input):
        for renderer in self.renderers:
            input = renderer.render(input)
        return input


class ParagraphRenderer:
    """From the Markdown documentation:

       A paragraph is simply one or more consecutive lines of text, separated
       by one or more blank lines."""

    def __init__(self):
        pass

    def render(self, input):
        return re.sub('(\n{2,})((\s|.)+)(\n{2,})',
                      '\\1<p>\\2</p>\\4',
                      input)


class HeaderRenderer:
    """
    """

    def __init__(self):
        self.headers = [('<h1>', '</h1>'),
            ('<h2>', '</h2>'),
            ('<h3>', '</h3>'),
            ('<h4>', '</h4>'),
            ('<h5>', '</h5>'),
            ('<h6>', '</h6>')]

    def _to_header(self, match):
        header = self.headers[len(match.group(1)) - 1]
        return header[0] + match.group(2) + header[1] + '\n'

    def render(self, input):
        return re.sub('^(#{1,6})[ ](\S.+)\n',
                      self._to_header,
                      input)


class EmphasisRenderer:
    """ """

    def __init__(self):
        pass

    def render(self, input):
        return re.sub('(?P<star>[\*_])(.+)(?P=star)',
                      '<em>\\2</em>',
                      input)