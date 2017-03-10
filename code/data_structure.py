#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is code from the OSM Case Study - Iterative Parsing Lesson. It's been
modified to reflect working on a local environment.

"""

import xml.etree.cElementTree as ET
import pprint

def count_tags_and_children(filename):
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

            # Make a dictionary of the child elements and their counts and attrs
            children = child_dict(elem)
            if children:
                for child, values in children.iteritems():
                    if child in tags[elem.tag]:
                        tags[elem.tag][child]['count'] += values['count']
                        for attr, attr_num in values['attributes'].iteritems():
                            tags[elem.tag][child]["attributes"][attr] += attr_num

                    # The child tag dictionary may not have been created by a
                    # previous else block, so create it now if we need too
                    else:
                        tags[elem.tag][child] = {}
                        tags[elem.tag][child]['count'] = values['count']
                        tags[elem.tag][child]["attributes"] = {}
                        for attr, attr_num in values['attributes'].iteritems():
                            tags[elem.tag][child]["attributes"][attr] = attr_num

        #If the tag isn't in the dictionary, add it as a dictionary
        else:
            tags[elem.tag] = {}
            tags[elem.tag]["count"] = 1
            children = child_dict(elem)
            if children:
                for child, values in children.iteritems():
                    tags[elem.tag][child] = {}
                    tags[elem.tag][child]['count'] = values['count']
                    tags[elem.tag][child]["attributes"] = {}
                    for attr, attr_num in values['attributes'].iteritems():
                        tags[elem.tag][child]["attributes"][attr] = attr_num
    return tags


def child_dict(element):
    '''
    return a dictionary of children and their attributes for each element
    '''
    children = {}
    for child in element:
        if child.tag in children:
            children[child.tag]["count"] += 1
            attrs = attrib_list(child)
            for attr in attrs:
                children[child.tag]["attributes"][attr] += 1
        
        else:
            children[child.tag] = {}
            children[child.tag]["count"] = 1
            children[child.tag]["attributes"] = {}
            attrs = attrib_list(child)
            for attr in attrs:
                children[child.tag]["attributes"][attr] = 1
    return children


def attrib_list(element):
    '''
    return the list of attributes for each element
    '''
    attrs = []
    for attr in element.attrib:
        attrs.append(attr)
    return attrs


def test(filename):
    tags = count_tags_and_children(filename)
    pprint.pprint(tags)


if __name__ == "__main__":
    test("../data/la-final.osm")
