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

With HSO, you can learn about many different things like Moving Averages, MACD, RSI, and Bollinger Bands.

I encourage you to point this repo to your favourite AI chat bot, and ask it questions, and help you learn, beginning with the question "What is HSO and should I learn it if I am interested in learning about investing?"

Happy hunting 🖖

sprezzarete

## Formula
### $HSO = SMAC + MACD5S_{sig} + MACD5S_{trend} + RSI + BB \in {-5, 5}$
### SMAC (Simple Moving Average Composite)
A weighted combination of price vs. MAs and MA vs. MA relationships where we represent each MA relationship as a sign function:
  
$'  S_{i,j} = \text{sgn}(MA_i - MA_j), \quad S_{i,P} = \text{sgn}(P - MA_i)'$

where

the vector of MA signals be:
  
$'  \mathbf{s} =
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
  \end{bmatrix}'$

the weight of MA signals be:
  
$'  \mathbf{w} =
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
  \end{bmatrix}'$

So the SMAC score is:
  
$'  \text{SMAC} = \text{Norm}\big(\mathbf{w}^\top \mathbf{s}\big) \in [-3, 3]'$
---
In summary:
  
$'  \text{SMAC} = \text{Normalization}\Bigg(
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
\in [-3, 3]'$

### MACD 5-day Signal Line Slope
$'MACD5S_{sig} =
  \begin{cases}
  +1 & \text{if slope of MACD signal line over last 5 days} > 0 \\
  0 & \text{otherwise}
  \end{cases}
\in \{0, 1\}'$

### MACD 5-day Trend Line Slope
$'MACD5S_{trend} =
  \begin{cases}
  +1 & \text{if slope of MACD trend line over last 5 days} > 0 \\
  0 & \text{otherwise}
  \end{cases}
\in \{0, 1\}'$

### RSI
$'RSI =
  \begin{cases}
  +0.5 & \text{if RSI < 30 (oversold)} \\
  -0.5 & \text{if RSI > 80 (overbought)} \\
  0 & \text{otherwise}
  \end{cases}
\in \{-0.5, 0, +0.5\}'$

### Bollinger Band
$'BB =
  \begin{cases}
  +0.2 & \text{if Price < LowerBand (2σ breach)} \\
  -0.2 & \text{if Price > UpperBand (2σ breach)} \\
  0 & \text{otherwise}
  \end{cases}
\in \{-0.2, 0, +0.2\}'$

## Backtest
Using an equal-weighted HSO, we run the following rules:

< 0: 100% SPY
>= 0 && <= 4: X% UPRO, (100 - X) SPY
> 4: Y% UPRO, (100 - Y) SPY

where X > Y



**Non-proprietary reference implementation** of the HSO for research and education.
- Indicator built from binary comparisons between price and multiple MAs, and between MAs.
- Produces a **bounded oscillator** in [-5, 5] and an **integer regime code**.
- Pluggable **encoding order** and **weighting** strategies.
- Minimal plotting utilities and a toy backtester.

## Quickstart

```bash
pip install -e .
python examples/example_usage.py --csv examples/sample_prices.csv --col price --sma 10 20 50 100
```

## CLI

```bash
python -m hso --csv examples/sample_prices.csv --col price --sma 10 20 50 100
```
