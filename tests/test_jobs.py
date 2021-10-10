import pytest

from jobs.jobsearch import (
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
    monster,
    linkedin
)

def job_search(response):
	return (
		isinstance(response, list)
		and len(response) > 1
	)

def test_lawjobs():
    query = "attorney"
    page = 1
    response = lawjobs(query,page)
    assert job_search(response)
	
def test_indeed():
    query = "Software Engineer"
    page = 1
    response = indeed(query,page)
    assert job_search(response)

def test_simplehired():
    query = "consultant"
    page = 1
    response = simplehired(query,page)
    assert job_search(response)

def test_craigslist():
    query = "researcher"
    region_id = "newyork"
    response = craigslist(query,region_id)
    assert job_search(response)

def test_craigslist_regions():
    response = craigslist_regions()
    assert (
            isinstance(response, list)
            and len(response) > 20
            )

def test_careerjet():
    query = "penetration tester"
    page = 1
    response = careerjet(query,page)
    assert job_search(response)

def test_dice():
    query = "penetration tester"
    page = 1
    response = dice(query,page)
    assert job_search(response)

def test_glassdoor():
    query = "penetration tester"
    page = 1
    response = glassdoor(query,page)
    assert job_search(response)

def test_xing():
    query = "penetration tester"
    page = 1
    response = xing(query,page)
    assert job_search(response)

def test_stackoverflow():
    query = "penetration tester"
    page = 1
    response = stackoverflow(query,page)
    assert job_search(response)

def test_monster():
    query = "penetration tester"
    state = "CA"
    response = monster(query,state)
    assert job_search(response)

def test_linkedin():
    query = "penetration tester"
    page = 1
    response = linkedin(query,page)
    assert job_search(response)
