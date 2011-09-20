#!/usr/bin/python
from tabloid import read_tabloid_metadata, Tabloid

def main():
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
    for post in tabloid.posts:
        print "<h1>%s</h1>" % post.metadata.title
        print
        print post.render()
    print "  </body>"
    print "</html>"

if __name__ == "__main__":
    main()
