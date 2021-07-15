from cachetools.func import ttl_cache
from latticestockdataclient.util.ttlcache import hourly_cache
from latticestockdataclient.util.LatticeStockDataAccessor import LatticeStockDataAccessor


class LatticeStockValuationDataClient:
    def __init__(self, lsda=None):
        self.lsda = lsda or LatticeStockDataAccessor()

    @hourly_cache
    def cost_of_equity(self, ticker_symbol):
        return self.lsda.get_json("/stock/valuation/cost-of-equity", {"ticker_symbol": ticker_symbol})["cost_of_equity"]

    @hourly_cache
    def enterprise_value(self, ticker_symbol):
        return self.lsda.get_json("/stock/valuation/enterprise-value", {"ticker_symbol": ticker_symbol})["enterprise_value"]

    @hourly_cache
    def historical_valuation_measures_table(self, ticker_symbol):
        return self.lsda.get_df("/stock/valuation/historical-valuation-measures", {"ticker_symbol": ticker_symbol})

    @hourly_cache
    def current_valuation_measures(self, ticker_symbol):
        return self.lsda.get_json("/stock/valuation/valuation-measures", {"ticker_symbol": ticker_symbol})

    def forward_pe(self, ticker_symbol):
        return self.current_valuation_measures(ticker_symbol)["Forward P/E"]

    def trailing_pe(self, ticker_symbol):
        return self.current_valuation_measures(ticker_symbol)["Trailing P/E"]

    def market_cap(sticker, ticker_symbol):
        return self.current_valuation_measures(ticker_symbol)["Market Cap (intraday)"]

