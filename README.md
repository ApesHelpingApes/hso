# Health Score Oscillator (HSO) – Open Source

**Non-proprietary reference implementation** of the HSO idea for research and education.
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
