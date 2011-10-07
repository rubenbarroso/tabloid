#!/usr/bin/python
import pickle
from tabloid import Tabloid
from os.path import join

def main():
    tabloid = Tabloid()
    paginator = tabloid.get_paginator()

    if paginator.is_not_empty():
        for post in paginator.get_all():
            print "Post:", post.metadata.title
            cached_contents_pathname = join(post.metadata.location, ".cached_contents")
            contents = post.read_content()
            with open(cached_contents_pathname, "w") as cached_contents:
                pickle.dump(contents, cached_contents)

if __name__ == "__main__":
    main()
