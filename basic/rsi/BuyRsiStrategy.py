"""
Algorithm Specifications
Long
    If RSI below or equal 30
Close
    If longer than 24 ticks
    If RSI is greater or equal 70
"""
"""
Total Trades 569
Average Win 2.00%
Average Loss -1.83%
Compounding Annual Return 3.989%
Drawdown 29.900%
Expectancy 0.179
Net Profit 124.765%
Sharpe Ratio 0.4
PSR 0.282%
Loss Rate 44%
Win Rate 56%
Profit-Loss Ratio 1.09
Alpha 0.017
Beta 0.366
Annual Standard Deviation 0.118
Annual Variance 0.014
Information Ratio -0.221
Tracking Error 0.156
Treynor Ratio 0.129
Total Fees $4658.47
"""
class SimpleRsiStrategy(QCAlgorithm):
    def Initialize(self):
        # Variable parameters
        self.traded_equity = "SPY"
        self.periods_since_last_trade = 0
        self.SetStartDate(2000, 1, 1)
        self.SetEndDate(2020, 9, 9)
        self.SetCash(100000)

        # Equity parameters - Traded equity and ticker timeframe
        self.AddEquity(self.traded_equity, Resolution.Hour)
        self.rsi = self.RSI(self.traded_equity, 14)
    def OnData(self, data):
        # Checking if RSI is usable
        if not self.rsi.IsReady:
            return

        if self.periods_since_last_trade == 24:
            # Close out positions if it goes on for more than a day
            self.Liquidate()
            self.periods_since_last_trade = -1
        elif self.rsi.Current.Value <= 30 and self.Portfolio[self.traded_equity].Invested == 0:
            # Long as RSI is below 30
            self.Liquidate()
            self.SetHoldings(self.traded_equity, 1)
            self.periods_since_last_trade = -1
        elif self.rsi.Current.Value >= 70:
            # Close position RSI is above 70
            self.Liquidate()
            self.periods_since_last_trade = -1

        # Incrementing days since last trade
        self.periods_since_last_trade += 1

    def OnEndOfDay(self):
        self.Plot("Indicators","RSI", self.rsi.Current.Value)
