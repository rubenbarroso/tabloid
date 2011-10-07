#!/usr/bin/python
import cgi
import cgitb
import md5
import urllib
from post import with_timestamp, with_category
from tabloid import Tabloid

cgitb.enable()

def main():
    form = cgi.FieldStorage()

    tabloid = Tabloid()

    if "alt" in form:
        print 'Content-type: application/atom+xml'
        print
        print '<?xml version="1.0" encoding="utf-8"?>'
        print '<feed xmlns="http://www.w3.org/2005/Atom">'
        print '  <title>TICS</title>'
        print '  <link href="http://ticsblog.com/"/>'
        print '  <updated>2003-12-13T18:30:02Z</updated>'
        print '  <author>'
        print '    <name>Ruben Barroso</name>'
        print '    <email>ruben.bm@gmail.com</email>'
        print '  </author>'
        print '  <id>http://ticsblog.com</id>'
        print '  <rights> (c) 2011 Ruben Barroso</rights>'
        for post in tabloid.get_paginator().get_page():
            print '  <entry>'
            print '    <title>%s</title>' % post.metadata.title
            print '    <link href="?alt=atom"/>'
            print '    <id>%s</id>' % md5.new(post.metadata.title).hexdigest()
            print '    <updated>2003-12-13T18:30:02Z</updated>'
            print '    <summary>This is a summary</summary>'
            print '  </entry>'
        print '</feed>'

        # stop rendering the feed
        return

    # headers
    # Nice google webfonts: Lekton, Jura
    print 'Content-type: text/html'
    print
    print '<html>'
    print '  <head>'
    print '    <link rel="stylesheet" type="text/css" href="tabloid.css" />'
    print '    <link rel="stylesheet" type="text/css" href="http://fonts.googleapis.com/css?family=Lekton">'
    print '    <title>%s</title>' % tabloid.title()
    print '  </head>'
    print '  <body>'
    print '<a href="/index.cgi">Home</a>', '<a href="?alt=atom">RSS</a>'
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
    if "page" in form:
        page_number = int(form.getvalue("page"))
    else:
        page_number = 0

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
