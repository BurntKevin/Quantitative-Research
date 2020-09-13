"""
Algorithm Specifications
Long
    If RSI below or equal 30
Short
    If RSI above or equal 70
Close
    If longer than 3.428 days
"""
"""
Algorithm Performance
Total Trades 1339
Average Win 1.54%
Average Loss -1.22%
Compounding Annual Return 3.604%
Drawdown 42.400%
Expectancy 0.105
Net Profit 108.146%
Sharpe Ratio 0.339
PSR 0.115%
Loss Rate 51%
Win Rate 49%
Profit-Loss Ratio 1.26
Alpha 0.025
Beta 0.244
Annual Standard Deviation 0.134
Annual Variance 0.018
Information Ratio -0.187
Tracking Error 0.194
Treynor Ratio 0.186
Total Fees $11412.71
"""
class SimpleRsiStrategy(QCAlgorithm):
    def Initialize(self):
        # Variable parameters
        self.tradedEquity = "SPY"
        self.maximumPeriodSinceLastTrade = 24
        self.periodSinceLastTrade = 0
        self.SetStartDate(2000, 1, 1)
        self.SetEndDate(2020, 9, 9)
        self.SetCash(100000)

        # Equity parameters - Traded equity and ticker timeframe
        self.AddEquity(self.tradedEquity, Resolution.Hour)
        self.rsi = self.RSI(self.tradedEquity, 14)
    def OnData(self, data):
        # Checking if RSI is usable
        if not self.rsi.IsReady:
            return

        if self.rsi.Current.Value <= 30 and self.Portfolio[self.tradedEquity].Quantity <= 0:
            # Long as RSI is below 30 (if not already long)
            self.SetHoldings(self.tradedEquity, 1)
            self.periodSinceLastTrade = 0
        elif self.rsi.Current.Value >= 70 and self.Portfolio[self.tradedEquity].Quantity >= 0:
            # Short as RSI is above 70 (if not already short)
            self.SetHoldings(self.tradedEquity, -1)
            self.periodSinceLastTrade = 0
        elif self.maximumPeriodSinceLastTrade == self.periodSinceLastTrade:
            # Close out positions if it goes on for too long
            self.Liquidate(self.tradedEquity)
            self.periodSinceLastTrade = 0

        # Incrementing days since last trade
        self.periodSinceLastTrade += 1

    def OnEndOfDay(self):
        self.Plot("Indicators", "RSI", self.rsi.Current.Value)
