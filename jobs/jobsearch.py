from jobs.get import get_json

def lawjobs(query, page=1):
	params = {"query": query, "page": page}
	return get_json("/lawjobs/search", params).get("jobs")

def indeed(query, page=1):
	params = {"query": query, "page": page}
	return get_json("/indeed/search", params).get("jobs")

def simplehired(query, page=1):
	params = {"query": query,"page": page}
	return get_json("/simplyhired/search", params).get("jobs")

def craigslist(query, region_id, page=1):
	params = {"query": query, "region_id": region_id, "page": page}
	return get_json("/craigslist/search", params).get("jobs")

def craigslist_regions():
	return get_json("/craigslist/regions").get("regions")

def careerjet(query, page=1):
	params = {"query": query, "page": page}
	return get_json("/careerjet/search", params).get("jobs")

def dice(query, page=1):
	params = {"query": query, "page": page}
	return get_json("/dice/search", params).get("jobs")

def glassdoor(query, page=1):
	params = {"query": query, "page": page}
	return get_json("/glassdoor/search", params).get("jobs")

def xing(query,page=1):
	params = {"query": query, "page": page}
	return get_json("/xing/search", params).get("jobs")

def stackoverflow(query, page=1):
	params = {"query": query, "page": page}
	return get_json("/stackoverflow/search", params).get("jobs")

def monster(query, state=None, page=1):
	params = {"query": query, "state": state, "page": page}
	return get_json("/monster/search", params).get("jobs")

def linkedin(query, page=1):
	params = {"query": query,"page": page}
	return get_json("/linkedin/search", params).get("jobs")
