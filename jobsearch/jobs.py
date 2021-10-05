from jobsearch.util.get import get_json

def lawjobs(query):
	params = {"query": query}
	return get_json("/lawjobs/search", params)

def indeed(query):
	params = {"query": query}
	return get_json("/indeed/search", params)

def simplehired(query):
	params = {"query": query}
	return get_json("/simplyhired/search", params)

def craigslist(query,region_id):
	params = {"query": query, "region_id": region_id}
	return get_json("/craigslist/search", params)

def craigslist_regions():
    return get_json("/craigslist/regions")

def careerjet(query):
	params = {"query": query}
	return get_json("/careerjet/search", params)

def dice(query):
	params = {"query": query}
	return get_json("/dice/search", params)

def glassdoor(query):
	params = {"query": query}
	return get_json("/glassdoor/search", params)

def xing(query):
	params = {"query": query}
	return get_json("/xing/search", params)

def stackoverflow(query):
	params = {"query": query}
	return get_json("/stackoverflow/search", params)

def monster(query):
	params = {"query": query}
	return get_json("/monster/search", params)

def linkedin(query):
	params = {"query": query}
	return get_json("/linkedin/search", params)
