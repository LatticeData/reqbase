from cachetools.func import ttl_cache
from latticestockdataclient.util.ttlcache import daily_cache
from latticestockdataclient.util.get import *
#from latticestockdataclient.util.LatticeStockDataAccessor import LatticeStockDataAccessor
def company_profile(ticker_symbol):
        return get_json("/stock/company-info", {"ticker_symbol": ticker_symbol})

def sector(ticker_symbol):
	return company_profile(ticker_symbol).get("Sector")

def industry(ticker_symbol):
	return company_profile(ticker_symbol).get("Industry")

def business_description(ticker_symbol):
	return company_profile(ticker_symbol).get("Description")

def website_url(ticker_symbol):
	return company_profile(ticker_symbol).get("Website")

def full_time_employees(ticker_symbol):
	profile = company_profile(ticker_symbol)
	if "Full Time Employees" in profile:
		return int(profile["Full Time Employees"])
	else:
		return None

def country(ticker_symbol):
	return company_profile(ticker_symbol).get("Country")

def state(ticker_symbol):
	return company_profile(ticker_symbol).get("State")

def city(ticker_symbol):
	return company_profile(ticker_symbol).get("City")
