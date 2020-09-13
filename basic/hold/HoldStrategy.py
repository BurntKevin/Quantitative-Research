"""
Algorithm Specifications
Long
    All in on first day
"""
"""
Algorithm Performance
Total Trades 1
Average Win 0%
Average Loss 0%
Compounding Annual Return 6.089%
Drawdown 55.100%
Expectancy 0
Net Profit 240.034%
Sharpe Ratio 0.416
PSR 0.326%
Loss Rate 0%
Win Rate 0%
Profit-Loss Ratio 0
Alpha 0
Beta 0.997
Annual Standard Deviation 0.196
Annual Variance 0.039
Information Ratio -0.19
Tracking Error 0.001
Treynor Ratio 0.082
Total Fees $5.00
"""
class HoldStrategy(QCAlgorithm):
    def Initialize(self):
        # Default parameters
        self.SetStartDate(2000, 1, 1)
        self.SetEndDate(2020, 9, 9)
        self.tradedEquity = "SPY"

        # Equity data
        self.AddEquity(self.tradedEquity, Resolution.Hour)
    def OnData(self, data):
        if not self.Portfolio[self.tradedEquity].Invested:
            # Buy if not already owned
            self.SetHoldings(self.tradedEquity, 1)
