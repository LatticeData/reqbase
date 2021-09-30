import pytest

from jobsearch.jobs import (
    lawjobs,
    indeed,
    simplehired,
    craigslist,
    craigslist_regions,
    careerjet,
    dice,
    glassdoor,
    xing,
    stackoverflow,
    ziprecruiter,
    monster,
    linkedin
)

def job_search(response):
	return (
		(response["status"] == "success")
		and "jobs" in response
		and isinstance(response["jobs"], list)
		and len(response["jobs"]) > 1
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

def test_careerjet():
    query = "penetration tester"
    location = "detroit"
    response = careerjet(query,location)
    assert job_search(response)

def test_dice():
    query = "penetration tester"
    location = "detroit"
    response = dice(query,location)
    assert job_search(response)

def test_glassdoor():
    query = "penetration tester"
    location = "detroit"
    response = glassdoor(query,location)
    assert job_search(response)

def test_xing():
    query = "penetration tester"
    location = "detroit"
    response = xing(query,location)
    assert job_search(response)

def test_stackoverflow():
    query = "penetration tester"
    location = "detroit"
    response = stackoverflow(query,location)
    assert job_search(response)

def test_ziprecruiter():
    query = "penetration tester"
    location = "detroit"
    response = ziprecruiter(query,location)
    assert job_search(response)

def test_monster():
    query = "penetration tester"
    state = "CA"
    response = monster(query,state)
    assert job_search(response)

def test_linkedin():
    query = "penetration tester"
    location = "detroit"
    response = linkedin(query,location)
    assert job_search(response)