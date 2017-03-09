#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is code from the OSM Case Study - Iterative Parsing Lesson. It's been
modified to reflect working on a local environment.

"""

import xml.etree.cElementTree as ET
import pprint

def count_tags(filename):
    '''
    Count the tags and the tag attributes
    '''
    tree = ET.iterparse(filename)
    tags = {}
    for event, elem in tree:

        # Check if the tag is already in our tags dictionary, increase count
        # if it is
        if elem.tag in tags:
            tags[elem.tag]["count"] += 1
            attrs = attrib_dict(elem)

            # Increase count of the attributes of each tag
            for attr in attrs:
                tags[elem.tag][attr] += 1
        
        #If the tag isn't in the dictionary, add it as a dictionary
        else:
            tags[elem.tag] = {}
            tags[elem.tag]["count"] = 1
            attrs = attrib_dict(elem)

            # Add the attributes of each tag as a separate dictionary
            for attr in attrs:
                tags[elem.tag][attr] = 1
    return tags


def attrib_dict(element):
    '''
    return the list of attributes for each element
    '''
    attrs = {}
    for attr in element.attrib:
        attrs[attr] = 1
    return attrs


def test(filename):

    tags = count_tags(filename)
    pprint.pprint(tags)
    

if __name__ == "__main__":
    test("../data/la-small.osm")


# assert tags == {'bounds': 1,
#                  'member': 3,
#                  'nd': 4,
#                  'node': 20,
#                  'osm': 1,
#                  'relation': 1,
#                  'tag': 7,
#                  'way': 1}