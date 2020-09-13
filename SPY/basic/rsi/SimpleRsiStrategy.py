"""
Algorithm Specifications
Long
    If RSI below or equal 30
Short
    If RSI above or equal 70
Close
    If longer than 24 ticks
"""
"""
Algorithm Performance
Total Trades 5908
Average Win 0.63%
Average Loss -0.32%
Compounding Annual Return 1.090%
Drawdown 51.800%
Expectancy 0.039
Net Profit 25.164%
Sharpe Ratio 0.149
PSR 0.005%
Loss Rate 65%
Win Rate 35%
Profit-Loss Ratio 1.94
Alpha 0.004
Beta 0.205
Annual Standard Deviation 0.138
Annual Variance 0.019
Information Ratio -0.299
Tracking Error 0.205
Treynor Ratio 0.1
Total Fees $39993.56
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
        elif self.rsi.Current.Value <= 30 and self.Portfolio[self.traded_equity].Invested <= 0:
            # Long as RSI is below 30 (if not already long)
            self.Liquidate()
            self.SetHoldings(self.traded_equity, 1)
            self.periods_since_last_trade = -1
        elif self.rsi.Current.Value >= 70 and self.Portfolio[self.traded_equity].Invested >= 0:
            # Short as RSI is above 70 (if not already short)
            self.Liquidate()
            self.SetHoldings(self.traded_equity, -1)
            self.periods_since_last_trade = -1

        # Incrementing days since last trade
        self.periods_since_last_trade += 1

    def OnEndOfDay(self):
        self.Plot("Indicators","RSI", self.rsi.Current.Value)
