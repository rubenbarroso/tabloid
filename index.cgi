#!/usr/bin/python
import cgi
import cgitb
import urllib
from post import with_timestamp, with_category
from tabloid import Tabloid

cgitb.enable()

def main():
    form = cgi.FieldStorage()

    if "page" in form:
        page_number = int(form.getvalue("page"))
    else:
        page_number = 0

    tabloid = Tabloid()

    # headers
    print "Content-type: text/html"
    print
    print "<html>"
    print "  <head>"
    print "    <title>%s</title>" % tabloid.title()
    print "  </head>"
    print "  <body>"
    print '<a href="/index.cgi">Home</a>'
    print

    # filter building
    filters = []

    extra_params = {}

    if "post" in form:
        timestamp = form.getvalue("post")
        filters.append(with_timestamp(timestamp))

    if "category" in form:
        category = form.getvalue("category")
        filters.append(with_category(category))
        extra_params['category'] = category

    # pagination
    paginator = tabloid.get_paginator(filters)
    if paginator.is_not_empty():
        for post in paginator.get_page(page_number):
            print post.render()

        previous_page = paginator.previous_page(page_number)
        if previous_page is not None:
            print '<a href="/index.cgi?%s"><< Newer posts</a>' % urllib.urlencode(
                    merge_dicts({"page": previous_page}, extra_params))

        next_page = paginator.next_page(page_number)
        if next_page is not None:
            print '<a href="/index.cgi?%s">Older posts >></a>' % urllib.urlencode(
                    merge_dicts({"page": next_page}, extra_params))
    else:
        print
        print "<p>No posts found.</p>"

    # footer
    print "  </body>"
    print "</html>"

def merge_dicts(dict1, dict2):
    return dict(dict1.items() + dict2.items())

if __name__ == "__main__":
    main()
