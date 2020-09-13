"""
Algorithm Specifications
Short
    If RSI greater or equal 70
Close
    If longer than 3.428 days
    If RSI is less or equal 30
"""
"""
Algorithm Performance
Total Trades 814
Average Win 1.08%
Average Loss -0.93%
Compounding Annual Return -0.210%
Drawdown 41.100%
Expectancy 0.000
Net Profit -4.251%
Sharpe Ratio 0.001
PSR 0.000%
Loss Rate 54%
Win Rate 46%
Profit-Loss Ratio 1.16
Alpha 0.009
Beta -0.114
Annual Standard Deviation 0.066
Annual Variance 0.004
Information Ratio -0.359
Tracking Error 0.228
Treynor Ratio -0.001
Total Fees $3836.30
"""
class SellRsiStrategy(QCAlgorithm):
    def Initialize(self):
        # Variable parameters
        self.tradedEquity = "SPY"
        self.maximumPeriodSinceLastTrade = 24
        self.periodSinceLastTrade = 0
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

        if self.rsi.Current.Value >= 70 and self.Portfolio[self.tradedEquity].Invested == 0:
            # Short as RSI is above 70
            self.SetHoldings(self.tradedEquity, -1)
            self.periodSinceLastTrade = 0
        elif self.rsi.Current.Value <= 30 or self.maximumPeriodSinceLastTrade == self.periodSinceLastTrade:
            # Close position as RSI is below 30 or if the position goes on for too long
            self.Liquidate()
            self.periodSinceLastTrade = 0

        # Incrementing days since last trade
        self.periodSinceLastTrade += 1

    def OnEndOfDay(self):
        self.Plot("Indicators", "RSI", self.rsi.Current.Value)
