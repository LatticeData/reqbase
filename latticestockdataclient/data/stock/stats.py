from cachetools.func import ttl_cache
from latticestockdataclient.util.ttlcache import hourly_cache
from latticestockdataclient.util.LatticeStockDataAccessor import LatticeStockDataAccessor


class LatticeStockStatsDataClient:
    def __init__(self, lsda=None):
        self.lsda = lsda or LatticeStockDataAccessor()

    @hourly_cache
    def key_stats_table(self, ticker_symbol):
        return self.lsda.get_json("/stock/key-stats", {"ticker_symbol": ticker_symbol})

    def beta(self, ticker_symbol):
        return self.key_stats_table(ticker_symbol)["Beta (5Y Monthly)"]

    def fifty_two_week_change(self, ticker_symbol):
        return self.key_stats_table(ticker_symbol)["52-Week Change"]

    def fifty_two_week_high(self, ticker_symbol):
        return self.key_stats_table(ticker_symbol)["52-Week High"]

    def fifty_two_week_low(self, ticker_symbol):
        return self.key_stats_table(ticker_symbol)["52-Week Low"]

    def fifty_day_moving_average(self, ticker_symbol):
        return self.key_stats_table(ticker_symbol)["50-Day Moving Average"]

    def two_hundred_day_moving_average(self, ticker_symbol):
        return self.key_stats_table(ticker_symbol)["200-Day Moving Average"]

    def three_month_average_volume(self, ticker_symbol):
        return self.key_stats_table(ticker_symbol)["Avg Vol (3 month)"]

    def ten_day_average_volume(self, ticker_symbol):
        return self.key_stats_table(ticker_symbol)["Avg Vol (10 day)"]

    def shares_outstanding(self, ticker_symbol):
        return self.key_stats_table(ticker_symbol)["Shares Outstanding"]

    def float_shares(self, ticker_symbol):
        return self.key_stats_table(ticker_symbol)["Float"]

    def percent_held_by_insiders(self, ticker_symbol):
        return self.key_stats_table(ticker_symbol)["% Held by Insiders"]

    def percent_held_by_institutions(self, ticker_symbol):
        return self.key_stats_table(ticker_symbol)["% Held by Institutions"]

     # 'Shares Short (Dec 14, 2020)': 94720000.0,
     # 'Short Ratio (Dec 14, 2020)': 1.0,
     # 'Short % of Float (Dec 14, 2020)': 0.005600000000000001,
     # 'Short % of Shares Outstanding (Dec 14, 2020)': 0.005600000000000001,
     # 'Shares Short (prior month Nov 12, 2020)': 87560000.0,

    def forward_annual_dividend_rate(self, ticker_symbol):
        return self.key_stats_table(ticker_symbol)["Forward Annual Dividend Rate"]

    def forward_annual_dividend_yield(self, ticker_symbol):
        return self.key_stats_table(ticker_symbol)["Forward Annual Dividend Yield"]

    def trailing_annual_dividend_rate(self, ticker_symbol):
        return self.key_stats_table(ticker_symbol)["Trailing Annual Dividend Rate"]

    def trailing_annual_dividend_yield(self, ticker_symbol):
        return self.key_stats_table(ticker_symbol)["Trailing Annual Dividend Yield"]
 
     # '5 Year Average Dividend Yield': 1.49,
     # 'Payout Ratio': 0.24239999999999998,
     # 'Dividend Date': {'$date': 1605052800000},
     # 'Ex-Dividend Date': {'$date': 1604534400000},
     # 'Last Split Factor': '4:1',
     #  'Last Split Date': {'$date': 1598745600000},
     # 'Fiscal Year Ends': {'$date': 1600992000000},
     # 'Most Recent Quarter (mrq)': {'$date': 1600992000000},
     # 'Profit Margin': 0.2091,
     # 'Operating Margin (ttm)': 0.2415,
     # 'Return on Assets (ttm)': 0.1251,
     # 'Return on Equity (ttm)': 0.7369,
     # 'Revenue (ttm)': 274519999999.99997,
     # 'Revenue Per Share (ttm)': 15.82,
     # 'Quarterly Revenue Growth (yoy)': 0.01,
     # 'Gross Profit (ttm)': 104960000000.0,
     # 'EBITDA': 77340000000.0,
     # 'Net Income Avi to Common (ttm)': 57410000000.0,
     # 'Diluted EPS (ttm)': 3.28,
     # 'Quarterly Earnings Growth (yoy)': -0.07400000000000001,
     # 'Total Cash (mrq)': 90940000000.0,
     # 'Total Cash Per Share (mrq)': 5.35,
     # 'Total Debt (mrq)': 122280000000.0,
     # 'Total Debt/Equity (mrq)': 187.14,
     # 'Current Ratio (mrq)': 1.36,
     # 'Book Value Per Share (mrq)': 3.85,
     # 'Operating Cash Flow (ttm)': 80670000000.0,
     # 'Levered Free Cash Flow (ttm)': 60390000000.0}

