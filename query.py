#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
For running queries against the MongoDB osm database la collection
"""
import sys

def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

# Create a sort query on count
def sort():
    sort = {"$sort" : {"count" : -1}}
    return sort

# Create a aggregation of tag types
def agg_types():
    group = {"$group" : {"_id" : "$type", "count" : {"$sum" : 1}}}
    return group

# Commands dictionary for converting string to function name
COMMANDS = {
    "sort" : sort,
    "agg_types" : agg_types
}

# Take the list of queries and make a query pipeline
def make_pipeline(list):
    # Complete the aggregation pipeline
    pipeline = []
    for arg in args:
        pipeline.append(COMMANDS[arg]())
    return pipeline

def tweet_sources(db, pipeline):
    return [doc for doc in db.la.aggregate(pipeline)]



if __name__ == '__main__':
    db = get_db('osm')
    args = list(sys.argv[1:])
    pipeline = make_pipeline(args)
    result = tweet_sources(db, pipeline)
    import pprint
    pprint.pprint(result)

