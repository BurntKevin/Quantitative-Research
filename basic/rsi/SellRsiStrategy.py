"""
Algorithm Specifications
Short
    If RSI greater or equal 70
Close
    If longer than 24 ticks
    If RSI is less or equal 30
"""
"""
Algorithm Performance
Total Trades 794
Average Win 1.12%
Average Loss -0.97%
Compounding Annual Return -0.821%
Drawdown 46.200%
Expectancy -0.033
Net Profit -15.700%
Sharpe Ratio -0.09
PSR 0.000%
Loss Rate 55%
Win Rate 45%
Profit-Loss Ratio 1.16
Alpha 0.004
Beta -0.12
Annual Standard Deviation 0.067
Annual Variance 0.004
Information Ratio -0.383
Tracking Error 0.229
Treynor Ratio 0.05
Total Fees $3522.92
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
        elif self.rsi.Current.Value <= 30:
            # Close position as RSI is below 30
            self.Liquidate()
            self.periods_since_last_trade = -1
        elif self.rsi.Current.Value >= 70 and self.Portfolio[self.traded_equity].Invested == 0:
            # Short as RSI is above 70
            self.Liquidate()
            self.SetHoldings(self.traded_equity, -1)
            self.periods_since_last_trade = -1

        # Incrementing days since last trade
        self.periods_since_last_trade += 1

    def OnEndOfDay(self):
        self.Plot("Indicators","RSI", self.rsi.Current.Value)
