#!/usr/bin/python
from tabloid import read_tabloid_metadata, Tabloid

def main():
    metadata = read_tabloid_metadata()

    print "Content-type: text/html"
    print

    print "<html><head>"
    print "<title>", metadata.title, "</title>"
    print "</head><body>"
    print "Tabloid was created by", metadata.author, "(c) 2011"
    print "</body></html>"

if __name__ == "__main__":
    main()
