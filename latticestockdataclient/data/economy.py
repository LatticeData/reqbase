from cachetools.func import ttl_cache
from latticestockdataclient.util.ttlcache import daily_cache
from latticestockdataclient.util.LatticeStockDataAccessor import LatticeStockDataAccessor


class LatticeStockEconomyDataClient:
    def __init__(self, lsda=None, prefix="/economy", host="stock-market-data.p.rapidapi.com", token=None):
        self.prefix = prefix
        self.host = host
        self.token = token
        self.lsda = lsda or LatticeStockDataAccessor(self.host, self.token)

    @daily_cache
    def risk_free_rate(self):
        return self.lsda.get_json(f"{self.prefix}/risk-free-rate")["risk_free_rate"]

    @daily_cache
    def last_year_market_return(self):
        return self.lsda.get_json(f"{self.prefix}/last-year-market-return")["last_year_market_return"]
