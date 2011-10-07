#!/usr/bin/python

def main():
    print 'Content-type: application/atom+xml'
    print
#    print '<html>'
#    print '  <head>'
#    print '    <title>Feed</title>'
#    print '  </head>'
#    print '  <body/>'

    print  """<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">

  <title>TICS</title>
  <link href="http://example.org/"/>
  <updated>2003-12-13T18:30:02Z</updated>
  <author>
    <name>Ruben Barroso</name>
    <email>ruben.bm@gmail.com</email>
  </author>
  <id>http://ticsblog.com</id>
  <rights> (c) 2011 Ruben Barroso</rights>

  <entry>
    <title>Atom-Powered Robots Run Amok</title>
    <link href="http://example.org/2003/12/13/atom03"/> <!-- a link to itself -->
    <id>urn:uuid:1225c695-cfb8-4ebb-aaaa-80da344efa6a</id>
    <updated>2003-12-13T18:30:02Z</updated>
    <summary>Some text.</summary>
  </entry>

</feed>"""

if __name__ == "__main__":
    main()
