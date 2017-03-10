#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
For running queries against the MongoDB osm database la collection

To run a query, navigate to this directory in your command line and run

python query.py [query COMMANDS]

make sure you have your DAND environment set in Conda
"""
import sys

def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

# Create a limit query
def limit():
    limit = {"$limit" : 1}
    return limit

# Create a sort query on count
def sort():
    sort = {"$sort" : {"count" : -1}}
    return sort

# Create a aggregation of tag types
def agg_types():
    group = {"$group" : {"_id" : "$tag_type",
                        "count" : {"$sum" : 1}}}
    return group

# Create a group for all user entries
def top_user():
    group = {"$group" : {"_id" : "$created.user",
                        "count" : {"$sum" : 1}}}
    return group

# Commands dictionary for converting string to function name
COMMANDS = {
    "limit" : limit,
    "sort" : sort,
    "agg_types" : agg_types,
    "top_user" : top_user
}

# Take the list of queries and make a query pipeline
def make_pipeline(args):
    # Complete the aggregation pipeline by iterating through the list of query
    # functions - args.
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

