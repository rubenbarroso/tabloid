#!/usr/bin/python
import cgi
import cgitb
import urllib
from tabloid import Tabloid

cgitb.enable()

def main():
    form = cgi.FieldStorage()

    if "page" in form:
        page_number = int(form.getvalue("page"))
    else:
        page_number = 0

    tabloid = Tabloid()
    tabloid.load()

    # blog headers
    print "Content-type: text/html"
    print
    print "<html>"
    print "  <head>"
    print "    <title>%s</title>" % tabloid.title()
    print "  </head>"
    print "  <body>"
    print "Tabloid was created by", tabloid.author(), "(c) 2011"
    print

    # single post rendering - test: 2011_09_16_15_50
    if "post" in form:
        post = tabloid.get_post(form.getvalue("post"))
        if post is not None:
            print
            print "<h1>%s</h1>" % post.metadata.title
            print
            print post.render()
            print
        else:
            print
            print "<p>Post not found.</p>"
    else:
        # paginated listing
        paginator = tabloid.get_paginator()
        for post in paginator.get_page(page_number):
            print
            print "<h1>%s</h1>" % post.metadata.title
            print
            print post.render()
            print

        previous_page = paginator.previous_page(page_number)
        if previous_page is not None:
            print '<a href="/index.cgi?%s"><< Newer posts</a>' % urllib.urlencode({"page": previous_page})

        next_page = paginator.next_page(page_number)
        if next_page is not None:
            print '<a href="/index.cgi?%s">Older posts >></a>' % urllib.urlencode({"page": next_page})

    print "  </body>"
    print "</html>"

if __name__ == "__main__":
    main()
