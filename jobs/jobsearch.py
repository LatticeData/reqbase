from jobs.get import get_json

def lawjobs(query,page=1):
	params = {"query": query,"page"=page}
	return get_json("/lawjobs/search", params)

def indeed(query,page=1):
	params = {"query": query,"page"=page}
	return get_json("/indeed/search", params)

def simplehired(query,page=1):
	params = {"query": query,"page"=page}
	return get_json("/simplyhired/search", params)

def craigslist(query,region_id):
	params = {"query": query, "region_id": region_id}
	return get_json("/craigslist/search", params)

def craigslist_regions():
    return get_json("/craigslist/regions")

def careerjet(query,page=1):
	params = {"query": query,"page"=page}
	return get_json("/careerjet/search", params)

def dice(query,page=1):
	params = {"query": query,"page"=page}
	return get_json("/dice/search", params)

def glassdoor(query,page=1):
	params = {"query": query,"page"=page}
	return get_json("/glassdoor/search", params)

def xing(query,page=1):
	params = {"query": query,"page"=page}
	return get_json("/xing/search", params)

def stackoverflow(query,page=1):
	params = {"query": query,"page"=page}
	return get_json("/stackoverflow/search", params)

def monster(query, state="CA"):
	params = {"query": query,"state"=state}
	return get_json("/monster/search", params)

def linkedin(query,page=1):
	params = {"query": query,"page"=page}
	return get_json("/linkedin/search", params)
