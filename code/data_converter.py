#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
import pprint
import re
import codecs
import json
import cleaning
"""
Description of script goes here
"""


lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')
skiptags = re.compile(r'(fixme)|(FIXME)|(is_in)|(gnis)|(FMMP)|(NHD)|(NHS)|(tiger)')

CREATED = [ "version", "changeset", "timestamp", "user", "uid"]

def creator_dict(attr):
    # Create and return dictionary of element's creator attributes
    created = {}
    for key in CREATED:
        created[key] = attr[key]
    return created





def shape_element(element):
    # Create main dictionary
    node = {}

    # Check element tag type, skipping tags, nds, and members
    if element.tag in ["node", "way", "relation"]:
        attr = element.attrib
        node['id'] = attr['id']
        node['tag_type'] = element.tag
        node['created'] = creator_dict(attr)

        # Node specific lat and lon list
        if element.tag == "node":
            node['pos'] = [float(attr['lat']), float(attr['lon'])]

        # Iterate over tags, nds, and members adding to node dict
        for child in element:
            tattr = child.attrib

            if child.tag == "member":
                member = {}
                for cattr in tattr:
                    member[cattr] = tattr[cattr]
                if 'member' in node:
                    node['member'].append(member)
                else:
                    node['member'] = []
                    node['member'].append(member)

            # Create list of refs for way tags
            elif child.tag == "nd":
                if 'node_refs' in node:
                    node['node_refs'].append(tattr['ref'])
                else:
                    node['node_refs'] = [tattr['ref']]

            # Add tags to node dictionary
            elif child.tag == "tag":
                # Skip problematic keys
                if problemchars.search(tattr['k']) or skiptags.search(tattr['k']):
                    continue

                # Split k values on first colon
                keys = tattr['k'].strip().split(':')

                # Add values to node dictionary
                if len(keys) > 1:
                    # Check and update city name:
                    if 'city' in keys[1]:
                        tattr['v'] = cleaning.check_city(tattr['v'])

                    if keys[0] == 'addr':
                        if 'address' in node:
                            node['address'].update({keys[1]: tattr['v']})
                        else:
                            node['address'] = {keys[1]: tattr['v']}
                    else:
                        if keys[0] in node:

                            # There may be a case where a prior child doesn't have
                            # a colon, but has the same key, so we need to reconfigure
                            # these elements as a dictionary
                            if type(node[keys[0]]) == 'str':
                                value = node[keys[0]]
                                node[keys[0]] = {'value': value}
                                node[keys[0]].update({keys[1]: tattr['v']})
                        else:
                            node[keys[0]] = {keys[1]: tattr['v']}
                else:
                    if keys[0] == 'colour':
                        node['color'] = tattr['v']
                        continue
                    node[keys[0]] = tattr['v']

        # Check the final node dict and clean any values
        if 'address' in node:
            if 'street_direction_prefix' in node['address']:
                street = cleaning.check_prefix(node)
                node['address']['street'] = street
                del node['address']['street_direction_prefix']

        return node
    else:
        return None


def process_map(file_in, pretty = False):
    # You do not need to change this file
    file_out = "{0}.json".format(file_in)
    data = []
    with codecs.open(file_out, "w") as fo:
        for _, element in ET.iterparse(file_in):
            el = shape_element(element)
            if el:
                data.append(el)
                if pretty:
                    fo.write(json.dumps(el, indent=2)+"\n")
                else:
                    fo.write(json.dumps(el) + "\n")
    return data

def test():
    # NOTE: if you are running this code on your computer, with a larger dataset, 
    # call the process_map procedure with pretty=False. The pretty=True option adds 
    # additional spaces to the output, making it significantly larger.
    data = process_map('../data/la-final.osm')
    #pprint.pprint(data)

if __name__ == "__main__":
    test()