# Health Score Oscillator (HSO)

## Question
What is the easiest and safest way to consistently beat the market?

## Answer
On a perpetuity timeline, apply leverage when we are most confident on positive returns because we accept:
- the market, empirically, is upward sloping over time
- Time in market > Timing the market
- Risk of underperformance > Comfort of lower drawdown
- Black-swan proof, if market doesn't recover, we have bigger problems

## Disclaimer
**Non-proprietary reference implementation** of the HSO for research and education.

___I AM NOT YOUR FINANCIAL ADVISOR ___

I am just a guy who is just trying to share something I have found useful. How you use it is entirely up to you.

With that out of the way...Hi, my name is Anthony!

From a very young age, my dad Joseph has instilled a love of stocks and trading. But more importantly, dad taught me we need to be responsible stewards of our wealth.

I have been blessed with a start in life that many can only dream about. And yet, for those who know me will attest, I didn't make my path the easiest for myself. I was my own worst enemy.

Like many people who witnessed the dot com boom, I was fascinated by internet trading...E-Trade!

I did so well I ended up getting myself a Porsche instead of a CLK when I was 25.

Fast forward a little bit, I got married, had a daughter, retired at 40, and relocated to Thailand.

I thought to myself, I am going to be, for the first time, a professional trader!

Now, let's be clear on one thing. All being a professional trader means is that I choose to make my living by trading. That's all it means.

Most importantly, being a professional trader doesn't automatically qualify me as good.

And to start being good, you need to be consistently profitable.

And not only consistently profitable, you need to _consistently beat the market_.

Or else, why bother 🤷

So, what I am trying to say is that, yeah, go try trading. Try learning all those fancy financial terms, including HSO.

Because _financial literacy_ is super important!

Like my dad taught me, we need to be responsible stewards of our wealth.

And that is true for everyone. You work hard for your money, so you should probably learn how to take care of your money.

And the truth is, investing is not _that_ hard.

You just need to get over yourself.

And accept that, no, you will most likely not be smarter than everyone else, and that, if you do try, you will most likely fail.

Because the US stocks market is _the most fascinating pool of people in the world_ and to have a sustainable edge that you can consistently beat this group of people is a fool's errand, and trying to do so is only because of 1 thing:

Ego

I developed HSO to try to help me outsmart the stock market. I made it fancy with things like lossless regime representation, trend detection, and blah, blah, blah.

It is patent pending.

But I am donating the license to Bridge the Gap Foundation because, like I said, financial literacy is important.

And from the HSO, I learned investing really isn't all that hard, just like what my dad taught me.

Your basic principles: start early, DCA, stay invested, and trust the market to do the work for you.

That's all there is to it.

With HSO, you can learn about many different things like [Moving Averages](https://www.investopedia.com/terms/m/movingaverage.asp), [MACD](https://www.investopedia.com/terms/m/macd.asp), [RSI](https://www.investopedia.com/terms/s/stochrsi.asp), and [Bollinger Bands](https://www.investopedia.com/terms/b/bollingerbands.asp).

I encourage you to point this repo to your favourite AI chat bot, and ask it questions, and help you learn, beginning with the question "What is HSO and should I learn it if I am interested in learning about investing?"

Happy hunting 🖖

sprezzarete

## Formula
### $HSO = SMAC + MACD5S_{sig} + MACD5S_{trend} + RSI + BB \in {-5, 5}$
### SMAC (Simple Moving Average Composite)
A weighted combination of price vs. MAs and MA vs. MA relationships where we represent each MA relationship as a sign function:
  
$S_{i,j} = \text{sgn}(MA_i - MA_j), \quad S_{i,P} = \text{sgn}(P - MA_i)$

where

the vector of MA signals be:

$$\mathbf{s} =
  \begin{bmatrix}
  S_{10,P} \\
  S_{50,P} \\
  S_{100,P} \\
  S_{200,P} \\
  S_{10,50} \\
  S_{10,100} \\
  S_{10,200} \\
  S_{50,100} \\
  S_{50,200} \\
  S_{100,200}
  \end{bmatrix}$$

the weight of MA signals be:
  
$$\mathbf{w} =
  \begin{bmatrix}
  W_{10,P} \\
  W_{50,P} \\
  W_{100,P} \\
  W_{200,P} \\
  W_{10,50} \\
  W_{10,100} \\
  W_{10,200} \\
  W_{50,100} \\
  W_{50,200} \\
  W_{100,200}
  \end{bmatrix}$$

So the SMAC score is:
  
$$\text{SMAC} = \text{Norm}\big(\mathbf{w}^\top \mathbf{s}\big) \in [-3, 3]$$
---
In summary:
  
$$\text{SMAC} = \text{Normalization}\Bigg( 
  W_{10,P} \cdot \text{sgn}(P - MA_{10}) + 
  W_{50,P} \cdot \text{sgn}(P - MA_{50}) + 
  W_{100,P} \cdot \text{sgn}(P - MA_{100}) + 
  W_{200,P} \cdot \text{sgn}(P - MA_{200}) + 
  W_{10,50} \cdot \text{sgn}(MA_{10} - MA_{50}) + 
  W_{10,100} \cdot \text{sgn}(MA_{10} - MA_{100}) + 
  W_{10,200} \cdot \text{sgn}(MA_{10} - MA_{200}) + 
  W_{50,1000} \cdot \text{sgn}(MA_{50} - MA_{100}) + 
  W_{50,200} \cdot \text{sgn}(MA_{50} - MA_{200}) + 
  W_{100,200} \cdot \text{sgn}(MA_{100} - MA_{200})
  \Bigg)
\in [-3, 3]$$

### MACD 5-day Signal Line Slope
$$MACD5S_{sig} =
  \begin{cases}
  +1 & \text{if slope of MACD signal line over last 5 days} > 0 \\
  0 & \text{otherwise}
  \end{cases}
\in \{0, 1\}$$

### MACD 5-day Trend Line Slope
$$MACD5S_{trend} =
  \begin{cases}
  +1 & \text{if slope of MACD trend line over last 5 days} > 0 \\
  0 & \text{otherwise}
  \end{cases}
\in \{0, 1\}$$

### RSI
$$RSI =
  \begin{cases}
  +0.5 & \text{if RSI < 30 (oversold)} \\
  -0.5 & \text{if RSI > 80 (overbought)} \\
  0 & \text{otherwise}
  \end{cases}
\in \{-0.5, 0, +0.5\}$$

### Bollinger Band
$$BB =
  \begin{cases}
  +0.2 & \text{if Price < LowerBand (2σ breach)} \\
  -0.2 & \text{if Price > UpperBand (2σ breach)} \\
  0 & \text{otherwise}
  \end{cases}
\in \{-0.2, 0, +0.2\}$$

## Backtest
Backtests are super important. Backtests are meaningless.

Both can be true.

Backtests are important to show how a particular model behaves based on historical data. It gives us an idea of what can potentially happen.

> [Lies, damned lies, and statsitics](https://en.wikipedia.org/wiki/Lies,_damned_lies,_and_statistics)

Benjamin Disraeli

You see, backtests give us a false sense of confidence. We tell ourselves, see, I have facts to prove my strategy!

But these facts and statistics are based on one thing: ***Start Date***

One can take the exact same strategy and start at different times and produce vastly different results. So is the strategy bad or is the strategy good 🤷‍♂️

What we do know is that:

***Time in market > Timing the market***

And picking a particular start date for a backtest exemplifies _timing the market_.

Research does show that [lump-sum](https://corporate.vanguard.com/content/dam/corp/research/pdf/cost_averaging_invest_now_or_temporarily_hold_your_cash.pdf) investment strategies beat most cost averaging investment strategies two-thirds of the time, so backtest does have some credibility, but again, results are subject to start date.

But realistically, most people most likely do not have a chunk of extra cash lying around doing nothing. Most people will be saving bit by bit, over many many years.

So naturally, it does make sense to [dollar-cost average (DCA)](https://www.investopedia.com/terms/d/dollarcostaveraging.asp)

And then when you add compound interest, [Albert Einstein's so called 8th wonder of the world](https://www.nasdaq.com/articles/this-is-the-8th-wonder-of-the-world-according-to-albert-einstein.-and-utilizing-it), investing really becomes _not that hard_.

So, backtests are important, and here we can backtest a simple strategy based off of a long-weighted SPY HSO:

```
< 0: 100% SPY
>= 0 && <= 4: X% UPRO, (100 - X) SPY
> 4: Y% UPRO, (100 - Y) SPY

where X > Y
```

### [QuantConnect](https://www.quantconnect.com)

Here's the [backtest](backtest_SPY_HSO.pdf) ready to be copied into QuantConnect

```
# QUANTCONNECT.COM - Democratizing Finance, Empowering Individuals.
# Lean Algorithmic Trading Engine Tied to Bridge Listings.
#
# Copyright 2014-2023 QuantConnect Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from AlgorithmImports import *

class HealthScoreStrategy(QCAlgorithm):
    def Initialize(self):
        """Initialise the data and resolution required, as well as the cash and start-end dates for your algorithm. All algorithms must initialized."""
        self.SetStartDate(2009, 7, 1) # UPRO inception date 6/25/09
        self.SetEndDate(2025, 8, 24)
        self.SetCash(1000)

        # --- ADD ASSETS ---
        self.spy = self.AddEquity("SPY", Resolution.Daily).Symbol
        self.SetBenchmark(self.spy)
        self.upro = self.AddEquity("UPRO", Resolution.Daily).Symbol

        # --- DEFINE INDICATORS FOR HSO ---
        # SMAC components
        self.sma10 = self.SMA(self.spy, 10, Resolution.Daily)
        self.sma50 = self.SMA(self.spy, 50, Resolution.Daily)
        self.sma100 = self.SMA(self.spy, 100, Resolution.Daily)
        self.sma200 = self.SMA(self.spy, 200, Resolution.Daily)

        # Other indicator components
        self.macd = self.MACD(self.spy, 12, 26, 9, MovingAverageType.Exponential, Resolution.Daily)
        self.rsi = self.RSI(self.spy, 14, MovingAverageType.Simple, Resolution.Daily)
        self.bb = self.BB(self.spy, 20, 2, MovingAverageType.Simple, Resolution.Daily)

        # History windows for MACD slope calculations
        self.macd_signal_history = RollingWindow[IndicatorDataPoint](6)
        self.macd_trend_history = RollingWindow[IndicatorDataPoint](6)
        
        # Warm up all indicators, plus 5 extra days for slope calculation
        self.SetWarmUp(205)

        # --- STRATEGY STATE VARIABLES ---
        self.health_score = 0

        # --- LONG-WEIGHTED HEALTH SCORE WEIGHTS (for SMAC component) ---
        self.weights = {
            "P-10": 0.1, "P-50": 0.2, "P-100": 0.3, "P-200": 0.4,
            "10-50": 0.2, "10-100": 0.3, "10-200": 0.4,
            "50-100": 0.3, "50-200": 0.4, "100-200": 0.4
        }


    def OnData(self, data: Slice):
        """OnData event is the primary entry point for your algorithm. Each new data point will be pumped in here."""
        # Update history windows before any calculations
        if self.macd.IsReady:
            self.macd_signal_history.Add(self.macd.Signal.Current)
            self.macd_trend_history.Add(self.macd.Current)

        if self.IsWarmingUp:
            return

        # --- CALCULATE CURRENT HEALTH SCORE ---
        self.health_score = self.calculate_health_score()
        self.Plot("Health Score", "HSO", self.health_score)

        # --- CORE PORTFOLIO ALLOCATION ---
        holdings = []
        uproAllocationTrending = .6
        uproAllocationEuphoria = .5
        if self.health_score < 0:
            # Participation
            holdings.extend([PortfolioTarget(self.spy, 1),
                PortfolioTarget(self.upro, 0)]) 
        elif self.health_score > 4:
            # Euphoria
            holdings.extend([PortfolioTarget(self.spy, (1 - uproAllocationEuphoria)),
                PortfolioTarget(self.upro, uproAllocationEuphoria)]) 
        else:
            # Trending
            holdings.extend([PortfolioTarget(self.spy, (1 - uproAllocationTrending)),
                PortfolioTarget(self.upro, uproAllocationTrending)]) 

        self.SetHoldings(holdings)
        pass
    

    def calculate_health_score(self):
        # 1. SMAC Score (Range: -3 to +3)
        # Doesn't normalize to 3 natively; assumes weighting will add to 3
        smac_score = 0.0
        price = self.Securities[self.spy].Price
        smac_score += (1 if price > self.sma10.Current.Value else -1) * self.weights["P-10"]
        smac_score += (1 if price > self.sma50.Current.Value else -1) * self.weights["P-50"]
        smac_score += (1 if price > self.sma100.Current.Value else -1) * self.weights["P-100"]
        smac_score += (1 if price > self.sma200.Current.Value else -1) * self.weights["P-200"]
        smac_score += (1 if self.sma10.Current.Value > self.sma50.Current.Value else -1) * self.weights["10-50"]
        smac_score += (1 if self.sma10.Current.Value > self.sma100.Current.Value else -1) * self.weights["10-100"]
        smac_score += (1 if self.sma10.Current.Value > self.sma200.Current.Value else -1) * self.weights["10-200"]
        smac_score += (1 if self.sma50.Current.Value > self.sma100.Current.Value else -1) * self.weights["50-100"]
        smac_score += (1 if self.sma50.Current.Value > self.sma200.Current.Value else -1) * self.weights["50-200"]
        smac_score += (1 if self.sma100.Current.Value > self.sma200.Current.Value else -1) * self.weights["100-200"]

        # 2. MACD Slope Scores (Range: 0 or +1 each)
        macd_sig_slope_score, macd_trend_slope_score = 0.0, 0.0
        if self.macd_signal_history.IsReady and self.macd_trend_history.IsReady:
            if self.macd_signal_history[0].Value > self.macd_signal_history[5].Value:
                macd_sig_slope_score = 1.0
            if self.macd_trend_history[0].Value > self.macd_trend_history[5].Value:
                macd_trend_slope_score = 1.0
    
        # 3. RSI Score (Range: -0.5, 0, +0.5)
        rsi_score = 0.0
        if self.rsi.IsReady:
            if self.rsi.Current.Value < 30:
                rsi_score = 0.5
            elif self.rsi.Current.Value > 80:
                rsi_score = -0.5
    
        # 4. Bollinger Band Score (Range: -0.2, 0, +0.2)
        bb_score = 0.0
        if self.bb.IsReady:
            if price < self.bb.LowerBand.Current.Value:
                bb_score = 0.2
            elif price > self.bb.UpperBand.Current.Value:
                bb_score = -0.2
            
        return smac_score + macd_sig_slope_score + macd_trend_slope_score + rsi_score + bb_score

```

## Quickstart
- Indicator built from binary comparisons between price and multiple MAs, and between MAs.
- Produces a **bounded oscillator** in [-5, 5] and an **integer regime code**.
- Pluggable **encoding order** and **weighting** strategies.
- Minimal plotting utilities and a toy backtester.

```bash
pip install -e .
python examples/example_usage.py --csv examples/sample_prices.csv --col price --sma 10 20 50 100
```

## CLI

```bash
python -m hso --csv examples/sample_prices.csv --col price --sma 10 20 50 100
```
