#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
For running queries against the MongoDB osm database la collection
"""
DIRECTIONS = {
	"N" : "North",
	"S" : "South",
	"E" : "East",
	"W" : "West"
}

ZIP_CHECK = {
	"91030" : "South Pasadena",
	"92627" : "Costa Mesa",
	"92570" : "Perris",
	"90210" : "Beverly Hills",
	"90089" : "University of Southern California"
}

def check_city(city_name):
    city = city_name.strip().title()
    return city

def check_prefix(node):
    prefix = node['address']['street_direction_prefix']
    prefix = DIRECTIONS[prefix]
    street = node['address']['street']
    return "%s %s" % (prefix, street)

def check_zip(node):
	zipcode = node['address']['postcode']
	city = node['address']['city']
	if ZIP_CHECK[zipcode] != 'city'
	return False

if __name__ == '__main__':
    cities = [' claremont', 'san gabriel ', ' yosemite', 'Glendale']
    for city in cities:
        print check_city(city)

