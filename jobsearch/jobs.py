from jobsearch.util.ttlcache import daily_cache
from jobsearch.util.get import *

@daily_cache
def lawjobs(query):
	params = {"query": query}
	return get_json("/lawjobs/search", params)

@daily_cache
def indeed(query):
	params = {"query": query}
	return get_json("/indeed/search", params)

@daily_cache
def simplehired(query):
	params = {"query": query}
	return get_json("/simplyhired/search", params)

@daily_cache
def craigslist(query,region_id):
	params = {"query": query, "region_id":region_id}
	return get_json("/craigslist/search", params)

@daily_cache
def craigslist_regions():
    return get_json("/craigslist/regions", params=None)