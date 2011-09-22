#!/usr/bin/python
import cgi
import cgitb
from tabloid import Tabloid

cgitb.enable()

def main():
    form = cgi.FieldStorage()
    id = "id" in form

    tabloid = Tabloid()
    tabloid.load()

    print "Content-type: text/html"
    print
    print "<html>"
    print "  <head>"
    print "    <title>%s</title>" % tabloid.title()
    print "  </head>"
    print "  <body>"
    print "Tabloid was created by", tabloid.author(), "(c) 2011"
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
