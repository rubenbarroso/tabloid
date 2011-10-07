import re

# TODO duplicated in tabloid module IMPORTANT
post_timestamp_pattern = re.compile('^\d{4}_\d{2}_\d{2}_\d{2}_\d{2}$')

class Renderer:
    """ """

    def __init__(self, post_location):
        self.renderers = [ParagraphRenderer(),
                          HeaderRenderer(),
                          EmphasisRenderer(),
                          ImageRenderer(post_location),
                          LinkRenderer()]

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
        paragraphs = ['<p>%s</p>\n\n' % x for x in re.split('\n{2,}', input) if x]
        return ''.join(paragraphs)


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
        return re.sub(r'(#{1,6})[ ](\S.+)\n',
                      self._to_header,
                      input)


class EmphasisRenderer:
    """ """

    def __init__(self):
        pass

    def render(self, input):
        return re.sub('(^|\s*|[ ]*)(?P<star>[\*_])([^_]+)(?P=star)([;, ])',
                      r'\1<em>\3</em>\4',
                      input)


class ImageRenderer:
    """This transforms ![alt text](/path/to/img.jpg "Title") into
       <img src="/path/to/img.jpg" alt="alt text" title="Title" />"""

    def __init__(self, post_location):
        self.post_location = post_location

    def render(self, input):
        return re.sub(r'!\[(.*)\]\(([^s]+)[ ]+"(.+)"\)',
                      r'<img src="%s%s\2" alt="\1" title="\3" />' % (self.post_location, "/images/"),
                      input)


class LinkRenderer:
    """[example link]() ->
    <a href="http://example.com/">example link</a>"""

    def __init__(self):
        pass

    def _to_link(self, match):
        def _is_post(dir):
            return not post_timestamp_pattern.match(dir) is None

        text = match.group(1)
        href = match.group(2)

        # internal or external link?
        if _is_post(href):
            return r'<a href="?post=%s">%s</a>' % (href, text)
        else:
            return '<a href="%s">%s</a>' % (href, text)

    def render(self, input):
        return re.sub(r'\[(.*)\]\(([^s]+)\)',
                      self._to_link,
                      input)
