"""
Algorithm Specifications
Long
    200 SMA above 50 SMA
Short
    200 SMA below 50 SMA
Close
    More than 14
"""
"""
Algorithm Performance
Total Trades 2912
Average Win 1.40%
Average Loss -1.34%
Compounding Annual Return -4.282%
Drawdown 67.900%
Expectancy -0.031
Net Profit -59.596%
Sharpe Ratio -0.135
PSR 0.000%
Loss Rate 53%
Win Rate 47%
Profit-Loss Ratio 1.05
Alpha -0.053
Beta 0.336
Annual Standard Deviation 0.19
Annual Variance 0.036
Information Ratio -0.487
Tracking Error 0.221
Treynor Ratio -0.076
Total Fees $9929.16
"""
class SimpleSmaStrategy(QCAlgorithm):
    def Initialize(self):
        # Default parameters
        self.tradedEquity = "SPY"
        self.SetStartDate(2000, 1, 1)
        self.SetEndDate(2020, 9, 9)
        self.SetCash(100000)
        self.slowPeriod = 200
        self.fastPeriod = 50
        self.periodSinceLastTrade = 0
        self.maximumperiodSinceLastTrade = 24

        # Analysis
        self.AddEquity(self.tradedEquity, Resolution.Hour)
        self.slowSma = self.SMA(self.tradedEquity, self.slowPeriod, Resolution.Hour)
        self.fastSma = self.SMA(self.tradedEquity, self.fastPeriod, Resolution.Hour)
    def OnData(self, data):
        # Checking if Sma indicator is ready
        if not self.fastSma.IsReady or not self.slowSma.IsReady:
            return

        if self.slowSma.Current.Value > self.fastSma.Current.Value and self.Portfolio[self.tradedEquity].Quantity <= 0:
            # Golden cross
            self.SetHoldings(self.tradedEquity, 1)
            self.periodSinceLastTrade = 0
        elif self.slowSma.Current.Value < self.fastSma.Current.Value and self.Portfolio[self.tradedEquity].Quantity >= 0:
            # Death cross
            self.SetHoldings(self.tradedEquity, -1)
            self.periodSinceLastTrade = 0

        if self.periodSinceLastTrade == self.maximumperiodSinceLastTrade:
            self.Liquidate()

        self.periodSinceLastTrade += 1

    def OnEndOfDay(self):
        self.Plot("Indicators", "Slow SMA", self.slowSma.Current.Value)
        self.Plot("Indicators", "Fast SMA", self.fastSma.Current.Value)
