import os
import json
from bson import json_util
import logging
import requests
import settings
from datetime import datetime, timedelta
from functools import wraps
import json
import requests
from io import StringIO

import pandas as pd

def get(url_path, params=None):
	if not params: params = {}
	url = "https://%s/%s" % (os.environ["STOCK_DATA_X_RAPID_API_HOST"].rstrip("/"), url_path.lstrip("/"))
	headers = {
		'x-rapidapi-key': os.environ["STOCK_DATA_X_RAPID_API_KEY"],
		'x-rapidapi-host': os.environ["STOCK_DATA_X_RAPID_API_HOST"]
	}
	return requests.get(url, headers=headers, params=params).text

def get_json(url_path, params=None):
	return json.loads(get(url_path, params=params))

def get_df(url_path, params=None):
	params["format"] = "csv"
	return pd.read_csv(StringIO(get(url_path, params=params)), index_col=0, parse_dates=True)