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
   # ziprecruiter,
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
    response = careerjet(query)
    assert job_search(response)

def test_dice():
    query = "penetration tester"
    response = dice(query)
    assert job_search(response)

def test_glassdoor():
    query = "penetration tester"
    response = glassdoor(query)
    assert job_search(response)

def test_xing():
    query = "penetration tester"
    response = xing(query)
    assert job_search(response)

def test_stackoverflow():
    query = "penetration tester"
    response = stackoverflow(query)
    assert job_search(response)

#def test_ziprecruiter():
 #   query = "penetration tester"
  #  location = "detroit"
   # response = ziprecruiter(query,location)
    #assert job_search(response)

def test_monster():
    query = "penetration tester"
    response = monster(query)
    assert job_search(response)

def test_linkedin():
    query = "penetration tester"
    response = linkedin(query)
    assert job_search(response)