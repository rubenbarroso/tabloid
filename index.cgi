#!/usr/bin/python
import cgi
import cgitb
from tabloid import read_tabloid_metadata, Tabloid

cgitb.enable()

def main():
    form = cgi.FieldStorage()
    id = "id" in form

    metadata = read_tabloid_metadata()
    tabloid = Tabloid(metadata)
    tabloid.load()

    print "Content-type: text/html"
    print
    print "<html>"
    print "  <head>"
    print "    <title>%s</title>" % metadata['title']
    print "  </head>"
    print "  <body>"
    print "Tabloid was created by", metadata['author'], "(c) 2011"
    print
    if id:
        print "Id: ", form.getvalue("id")
    else:
        print "Not Id found ha"
    for post in tabloid.posts:
        print "<h1>%s</h1>" % post.metadata.title
        print
        print post.render()
    print "  </body>"
    print "</html>"

if __name__ == "__main__":
    main()
