import pytest

from jobsearch.jobs import (
    lawjobs,
    indeed,
    simplehired,
    craigslist,
    craigslist_regions
)

def job_search(response):
	return (
		(response["status"] == "success")
		and "jobs" in response
		and isinstance(response["jobs"], list)
		and len(response["jobs"]) > 10
	)

def test_lawjobs():
    query = "attorney"
    response = lawjobs(query)
    assert job_search(response)
	
def test_indeed():
    query = "Software Engineer"
    response = indeed(query)
    assert job_search(response)

def test_simplehired():
    query = "consultant"
    response = simplehired(query)
    assert job_search(response)

def test_craigslist():
    query = "researcher"
    region_id = "newyork"
    response = craigslist(query,region_id)
    assert job_search(response)

def test_craigslist_regions():
    response = craigslist_regions()
    assert (
        	(response["status"] == "success")
            and "regions" in response
            and isinstance(response["regions"], list)
            and len(response["regions"]) > 20
            )