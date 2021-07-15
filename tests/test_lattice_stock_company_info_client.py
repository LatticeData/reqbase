import pytest
from latticestockdataclient.data.stock.company_info import *

ticker_symbol = "AAPl"
from latticestockdataclient.data.stock.company_info import (
    company_profile,
    sector,
    industry,
    business_description,
    website_url,
    full_time_employees,
    country,
    state,
    city

)

def test_company_profile():

    symbol = ticker_symbol

    data = company_profile(symbol)

    assert (

        data["status"] == "success"
        and data["company_profile"]["Sector"] == "Technology"
        and data["company_profile"]["Industry"] == "Consumer Electronics"
        and data["company_profile"]["Full Time Employees"] > 99999
        and data["company_profile"]["Description"] is not None
        and data["company_profile"]["Website"] == "http://www.apple.com"
        and data["company_profile"]["Country"] == "United States"
        and data["company_profile"]["State"] == "CA"
        and data["company_profile"]["City"] == "Cupertino"


    )