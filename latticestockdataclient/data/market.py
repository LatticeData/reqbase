from cachetools.func import ttl_cache
from latticestockdataclient.util.ttlcache import daily_cache
#from latticestockdataclient.util.LatticeStockDataAccessor import LatticeStockDataAccessor
from latticestockdataclient.util.get import *


@daily_cache
def s_and_p_composition():
    return get_json("/market/index/s-and-p-composition")["stocks"]

@daily_cache
def nasdaq_composition(self):
    return get_json("/market/index/nasdaq-composite")["stocks"]

@daily_cache
def dji_composition(self):
    return get_json("/market/index/dji-composition")["stocks"]

@daily_cache
def russel_one_thousand_composition(self):
    return get_json("/market/index/russel-one-thousand")["stocks"]
@daily_cache
    def amex_oil_composition(self):
        return get_json("/market/index/amex-oil-index")["stocks"]

@daily_cache
def djia_composition(self):
    return get_json("/market/index/djia")["stocks"]

@daily_cache
def bbc_global_composition(self):
    return get_json("/market/index/bbc-global-thirty")["stocks"]

@daily_cache
def ibovespa_composition(self):
    return get_json("/market/index/ibovespa")["stocks"]

@daily_cache
def ftse100_composition(self):
    return get_json("/market/index/ftse-one-hundred")["stocks"]

@daily_cache
def ftse250_composition(self):
    return get_json("/market/index/ftse-two-fifty")["stocks"]

@daily_cache
def nifty_fifty_composition(self):
    return get_json("/market/index/nifty-fifty")["stocks"]

@daily_cache
def djgt_fifty_composition(self):
    return get_json("/market/index/dow-jones-global-titans-fifty")["stocks"]

@daily_cache
def dax_thirty_composition(self):
    return get_json("/market/index/dax-thirty")["stocks"]

@daily_cache
def euro100_composition(self):
    return get_json("/market/index/euro-next-one-hundred")["stocks"]

@daily_cache
def djta_composition(self):
    return get_json("/market/index/down-jones-transportation-average")["stocks"]

@daily_cache
def djua_composition(self):
    return get_json("/market/index/down-jones-utility-average")["stocks"]

@daily_cache
def nasdaq100_composition(self):
    return get_json("/market/index/nasdaq-one-hundred")["stocks"]

@daily_cache
def phlx_semi_composition(self):
    return get_json("/market/index/phlx-semiconductor")["stocks"]

@daily_cache
def phlx_gold_composition(self):
    return get_json("/market/index/phlx-gold-and-silver")["stocks"]

@daily_cache
def nikkei225_composition(self):
    return get_json("/market/index/nikkei-two-twenty-five")["stocks"]

@daily_cache
def omx_nordic_composition(self):
    return get_json("/market/index/omx-nordic-forty")["stocks"]

@daily_cache
def nyse_arca_composition(self):
    return get_json("/market/index/nyse-arca-major-market-index")["stocks"]

@daily_cache
def all_public_companies(self):
    return get_json("/market/all-public-companies")["stocks"]

@daily_cache
def nasdaq_exchange_composition(self):
    return get_json("/market/exchange/nasdaq")["stocks"]

@daily_cache
def nyse_composition(self):
    return get_json("/market/exchange/nyse")["stocks"]

@daily_cache
def shanghai_exchange_composition(self):
    return get_json("/market/exchange/shanghai-stock-exchange")["stocks"]

@daily_cache
def hong_kong_exchange_composition(self):
    return get_json("/market/exchange/hong-kong-stock-exchange")["stocks"]

@daily_cache
def london_exchange_composition(self):
    return get_json("/market/exchange/london-stock-exchange")["stocks"]

@daily_cache
def conservative_foreign_funds(self):
    return get_json("/market/screener/conservative-foreign-funds")["funds"]

@daily_cache
def most_actives(self):
    return get_json("/market/screener/most-actives")["stocks"]

@daily_cache
def most_shorted_stocks(self):
    return get_json("/market/screener/most-shorted-stocks")["stocks"]

@daily_cache
def undervalued_growth_stocks(self):
    return get_json("/market/screener/undervalued-growth-stocks")["stocks"]

@daily_cache
def growth_technology_stocks(self):
    return get_json("/market/screener/growth-technology-stocks")["stocks"]

@daily_cache
def day_gainers(self):
    return get_json("/market/screener/day-gainers")["stocks"]

@daily_cache
def day_losers(self):
    return get_json("/market/screener/day-losers")["stocks"]

@daily_cache
def undervalued_large_caps(self):
    return get_json("/market/screener/undervalued-large-caps")["stocks"]

@daily_cache
def aggresive_small_caps(self):
    return get_json("/market/screener/aggressive-small-caps")["stocks"]

@daily_cache
def small_cap_gainers(self):
    return get_json("/market/screener/small-cap-gainers")["stocks"]

@daily_cache
def top_mutual_funds(self):
    return get_json("/market/screener/top-mutual-funds")["mutual_funds"]

@daily_cache
def portfolio_anchors(self):
    return get_json("/market/screener/portfolio-anchors")

@daily_cache
def solid_large_growth_funds(self):
    return get_json("/market/screener/solid-large-growth-funds")["funds"]

@daily_cache
def solid_midcap_growth_funds(self):
    return get_json("/market/screener/solid-midcap-growth-funds")["funds"]

@daily_cache
def high_yield_bonds(self):
    return get_json("/market/screener/high-yield-bonds")["bonds"]