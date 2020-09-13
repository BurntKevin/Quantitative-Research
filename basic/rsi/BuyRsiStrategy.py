"""
Algorithm Specifications
Long
    If RSI below or equal 30
Close
    If position held longer than 2 days
    If RSI is greater or equal 70
"""
"""
Algorithm Performance
Total Trades 569
Average Win 2.11%
Average Loss -1.70%
Compounding Annual Return 3.820%
Drawdown 25.200%
Expectancy 0.185
Net Profit 117.343%
Sharpe Ratio 0.388
PSR 0.229%
Loss Rate 47%
Win Rate 53%
Profit-Loss Ratio 1.24
Alpha 0.016
Beta 0.358
Annual Standard Deviation 0.117
Annual Variance 0.014
Information Ratio- 0.232
Tracking Error 0.157
Treynor Ratio 0.127
Total Fees $4263.28
"""
class BuyRsiStrategy(QCAlgorithm):
    def Initialize(self):
        # Variable parameters
        self.tradedEquity = "SPY"
        self.periodSinceLastTrade = 0
        self.maximumPeriodSinceLastTrade = 24
        self.SetStartDate(2000, 1, 1)
        self.SetEndDate(2020, 9, 9)
        self.SetCash(100000)

        # Equity parameters - Traded equity and timeframe
        self.AddEquity(self.tradedEquity, Resolution.Hour)
        self.rsi = self.RSI(self.tradedEquity, 14)
    def OnData(self, data):
        # Checking if RSI is usable
        if not self.rsi.IsReady:
            return

        if self.rsi.Current.Value <= 30 and self.Portfolio[self.tradedEquity].Invested == 0:
            # Long as RSI is below 30 and do not have a position yet
            self.SetHoldings(self.tradedEquity, 1)
            self.periodSinceLastTrade = 0
        elif self.periodSinceLastTrade == self.maximumPeriodSinceLastTrade or self.rsi.Current.Value >= 70:
            # Close out positions if it goes on for too long or RSI above 70
            self.Liquidate()
            self.periodSinceLastTrade = 0

        # Incrementing days since last trade
        self.periodSinceLastTrade += 1

    def OnEndOfDay(self):
        self.Plot("Indicators", "RSI", self.rsi.Current.Value)
