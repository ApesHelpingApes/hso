import numpy as np
import pandas as pd
from typing import List, Tuple, Sequence, Callable, Dict

def sma(series: pd.Series, window: int) -> pd.Series:
    return series.rolling(window=window, min_periods=window).mean()

def _pairs(indexes: Sequence[int]) -> List[Tuple[int,int]]:
    out = []
    for i in range(len(indexes)):
        for j in range(i+1, len(indexes)):
            out.append((indexes[i], indexes[j]))
    return out

def default_public_encoding(price: float, mas: Dict[int, float], order: List[Tuple[str, tuple]]) -> List[int]:
    """Produce binary bits according to a supplied order.
    Each element in order is either:
      ("P_GT_MA", ma_window)               -> 1 if price > ma
      ("MA_GT_MA", (ma_a, ma_b))           -> 1 if MA_a > MA_b
    Returns list of bits (1/0)."""
    bits = []
    for kind, obj in order:
        if kind == "P_GT_MA":
            w = obj
            v = 1 if price > mas[w] else 0
        elif kind == "MA_GT_MA":
            a,b = obj
            v = 1 if mas[a] > mas[b] else 0
        else:
            raise ValueError(f"Unknown encoding kind: {kind}")
        bits.append(v)
    return bits

def build_public_order(sma_windows: Sequence[int]) -> List[Tuple[str, tuple]]:
    # Public order: price>each MA (ascending), then all MA>MA pairs (ascending windows)
    order = []
    for w in sorted(sma_windows):
        order.append(("P_GT_MA", w))
    wins = sorted(sma_windows)
    for i in range(len(wins)):
        for j in range(i+1, len(wins)):
            order.append(("MA_GT_MA", (wins[i], wins[j])))
    return order

def to_regime_code(bits: Sequence[int]) -> int:
    code = 0
    N = len(bits)
    for i,b in enumerate(bits):
        code += (1 if b else 0) * (2**(N-1-i))
    return code

def to_signed(bits: Sequence[int]) -> np.ndarray:
    # bullish(1)->+1, bearish(0)->-1
    return np.array([1 if b==1 else -1 for b in bits], dtype=float)

def compute_hso(prices: pd.Series,
                sma_windows: Sequence[int],
                encoder: Callable = None,
                order: Sequence = None,
                weights: Sequence[float] = None):
    """Compute HSO score and regime for a price series.
    Returns (score_series, regime_series, dataframe_with_intermediates)."""
    prices = pd.Series(prices).astype(float)
    mas = {w: sma(prices, w) for w in sma_windows}
    if order is None:
        order = build_public_order(sma_windows)
    N = len(order)
    if encoder is None:
        encoder = default_public_encoding
    if weights is None:
        weights = np.ones(N) / N
    weights = np.asarray(weights, dtype=float)
    scores = []
    regimes = []
    for idx in range(len(prices)):
        if any(np.isnan(mas[w].iloc[idx]) for w in sma_windows):
            scores.append(np.nan); regimes.append(np.nan); continue
        p = prices.iloc[idx]
        cur_mas = {w: mas[w].iloc[idx] for w in sma_windows}
        bits = encoder(p, cur_mas, order)
        code = to_regime_code(bits)
        signed = to_signed(bits)
        raw = float(np.dot(signed, weights))
        scores.append(raw)
        regimes.append(code)
    frame = pd.DataFrame({"price": prices, "score": pd.Series(scores, index=prices.index), "regime": pd.Series(regimes, index=prices.index)})
    return frame["score"], frame["regime"], frame
