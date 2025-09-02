# Health Score Oscillator (HSO)

## Question
What is the safest way to consistently beat the market?

## Answer
On a perpetuity timeline, apply leverage when we are most confident on positive returns because we accept:
- the market, empirically, is upward sloping over time
- Time in market > Timing the market
- Risk of underperformance > Comfort of lower drawdown
- Black-swan proof, if market doesn't recover, we have bigger problems

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
