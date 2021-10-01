import os
import json
import logging
import requests
from io import StringIO

import pandas as pd
from dotenv import load_dotenv 

load_dotenv()

def get(url_path, params=None):
	if not params: params = {}
	host = "job-search4.p.rapidapi.com"
	url = "https://%s/%s" % (host.rstrip("/"), url_path.lstrip("/"))
	headers = {
		'x-rapidapi-key': os.environ["JOB_SEARCH_X_RAPID_API_KEY"],
		'x-rapidapi-host': host
	}
	return requests.get(url, headers=headers, params=params).text

def get_json(url_path, params=None):
	result = json.loads(get(url_path, params=params))
	if not result: result = {}
	return result

def get_df(url_path, params=None):
	params["format"] = "csv"
	return pd.read_csv(StringIO(get(url_path, params=params)), index_col=0, parse_dates=True)
