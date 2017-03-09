#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is code from the OSM Case Study - Iterative Parsing Lesson. It's been modified
to reflect working on a local environment.

"""

import xml.etree.cElementTree as ET
import pprint
import re

def count_tags(filename, tagtype):
    """Return a set of unique attribute values for k in the tag element"""
    tree = ET.iterparse(filename, events=('start',))
    tags = set()
    for event, elem in tree:
        if elem.tag == tagtype:
            for tag in elem.iter():
                if tag.tag == "tag":
                    tags.add(tag.attrib['k'])
    return tags

def tag_search(filename, tagtype, search):
    """Return a set of unique attribute values for k in the tag element"""
    tree = ET.iterparse(filename, events=('start',))
    tags = []
    for event, elem in tree:
        if elem.tag == tagtype:
            for tag in elem.iter():
                if tag.tag == "tag":
                    if re.search(search, tag.attrib['k']):
                        tags.append(tag.attrib)
    return tags

def test(filename):
    #tags = tag_search("./data/la-small.osm", "tag", "addr:street")
    #pprint.pprint(tags)
    tags = count_tags(filename, "relation")
    print "Node Tags:"
    pprint.pprint(tags)
    print ""
    
    #tags = count_tags(filename, "way")
    #print "Way Tags:"
    #pprint.pprint(tags)
    

if __name__ == "__main__":
    test("../data/la-small.osm")