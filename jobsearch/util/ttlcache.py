import os
import json
import logging
import requests
from datetime import datetime, timedelta
from functools import wraps
from cachetools.func import ttl_cache

def hourly_cache(func):
    @wraps(func)
    @ttl_cache(maxsize=1, ttl=60*60)
    def decorated_function(*args, **kwargs):
        return func(*args, **kwargs)
    return decorated_function

def daily_cache(func):
    @wraps(func)
    @ttl_cache(maxsize=1, ttl=24*60*60)
    def decorated_function(*args, **kwargs):
        return func(*args, **kwargs)
    return decorated_function
    
def weekly_cache(func):
    @wraps(func)
    @ttl_cache(maxsize=1, ttl=7*24*60*60)
    def decorated_function(*args, **kwargs):
        return func(*args, **kwargs)
    return decorated_function

