from latticestockdataclient.util.LatticeStockDataAccessor import LatticeStockDataAccessor
from latticestockdataclient.util.ttlcache import hourly_cache


class LatticeStockHistoricalDataClient:
    def __init__(self, lsda=None):
        self.lsda = lsda or LatticeStockDataAccessor()

    @hourly_cache
    def historical_prices(self, ticker_symbol, years=5):
        params = {"ticker_symbol": ticker_symbol, "years": years, "format": "csv"}
        return self.lsda.get_df("/stock/historical-prices", params)

