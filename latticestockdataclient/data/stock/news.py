from cachetools.func import ttl_cache
from latticestockdataclient.util.ttlcache import hourly_cache
from latticestockdataclient.util.LatticeStockDataAccessor import LatticeStockDataAccessor


class LatticeStockNewsDataClient:
    def __init__(self, lsda=None):
        self.lsda = lsda or LatticeStockDataAccessor()

    @hourly_cache
    def latest_company_news(ticker_symbol):
        return self.lsda.get_json("/stock/news", {"ticker_symbol": ticker_symbol})["articles"]

    @hourly_cache
    def latest_news_sentiment(self, ticker_symbol):
        return self.lsda.get_json("/stock/sentiment", {"ticker_symbol": ticker_symbol})["sentiment"]

