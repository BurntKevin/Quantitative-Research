# Focus
* Research focuses on SPY (S&P 500 ETF)
* Backtests done from the 1st of January 2000 to 9th of September 2020
* Trades are targetted to be closed within a week to avoid position taking, preferably 3.428 days
* Tested on 1 hour candles to allow sufficient time periods
* No overfitting is done, it will be based on initial ideas

# Potential Issues
* Historically SPY has shown positive growth and hence, long-term shorts are not great
* Statically testing 20 years of data means that increased market efficiency is not factored

# Important Considerations
* Effective compound rate is important as trading means that the capital is not always fully utilised

# General Findings
* It is difficult to beat the classic buy and hold strategy
* Strategies which go long more frequently outperform shorts
* Adding a maximum time period which a position is held pushes returns closer to 0
* Some strategies work great on a daily time frame but fail on an hourly time frame (but this may be due to longer position taking)
* Fees can take up a decent portion of revenue ranging from a minimum of 10% to over 100%
* Reducing the timeframe to a more contemporary span reduces returns which may indicate a more efficient market as time goes on for commonly used strategies

# Strategies
| Strategy                       | Trades | Profit-Loss Ratio | Expected Value | Win Ratio | Alpha  | Beta   | Sharpe Ratio | Drawdown | Compounded Annual Return |
|--------------------------------|--------|-------------------|----------------|-----------|--------|--------|--------------|----------|--------------------------|
| <b>HoldStrategy - Benchmark<b> | 1      | N/A               | N/A            | N/A       | N/A    | 0.997  | 0.416        | 55.100%  | 6.089%                   |
| BuyRsiStrategy                 | 569    | 1.24              | 0.3193%        | 53%       | 0.016  | 0.358  | 0.388        | 25.200%  | 3.820%                   |
| SimpleRsiStrategy              | 1339   | 1.26              | 0.1324%        | 49%       | 0.025  | 0.244  | 0.339        | 42.400%  | 3.604%                   |
| SellRsiStrategy                | 814    | 1.16              | -0.0054%       | 46%       | 0.009  | -0.114 | 0.001        | 41.100%  | -0.210%                  |
| SimpleSmaStrategy              | 2912   | 1.05              | -0.0522%       | 47%       | -0.053 | 0.336  | -0.135       | 67.900%  | -4.282%                  |

# Further Strategies: To Be Developed
* Gap Theory
  * What percentage of gaps are filled?
  * What percentage of up gaps are filled?
  * What percentage of down gaps are filled?
* Best Time To Buy
  * Period of Day
    * Start of day?
    * End of day?
    * Any other point?
  * Dividends
    * Before dividend day?
    * On dividend day?
    * After dividend day?
* Who Provides Growth?
  * Market capitalisation weighted or equal weighted
* Buy On Red Days
  * Close price then sell on next open
