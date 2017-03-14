#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
For running queries against the MongoDB osm database la collection
"""

def check_city(city_name):
    city = city_name.strip().title()
    return city

if __name__ == '__main__':
    cities = [' claremont', 'san gabriel ', ' yosemite', 'Glendale']
    for city in cities:
        print check_city(city)

