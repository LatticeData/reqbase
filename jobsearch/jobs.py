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

@daily_cache
def careerjet(query,location):
	params = {"query": query, "location":location}
	return get_json("/careerjet/search", params)

@daily_cache
def dice(query,location):
	params = {"query": query, "location":location}
	return get_json("/dice/search", params)

@daily_cache
def glassdoor(query,location):
	params = {"query": query, "location":location}
	return get_json("/glassdoor/search", params)

@daily_cache
def xing(query,location):
	params = {"query": query, "location":location}
	return get_json("/xing/search", params)

@daily_cache
def stackoverflow(query,location):
	params = {"query": query, "location":location}
	return get_json("/stackoverflow/search", params)

@daily_cache
def ziprecruiter(query,location):
	params = {"query": query, "location":location}
	return get_json("/ziprecruiter/search", params)

@daily_cache
def monster(query,state):
	params = {"query": query, "state":state}
	return get_json("/monster/search", params)

@daily_cache
def linkedin(query,location):
	params = {"query": query, "location":location}
	return get_json("/linkedin/search", params)