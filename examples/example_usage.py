# Example usage script
import numpy as np, pandas as pd
from hso.core import compute_hso
from hso.weights import EqualWeights

prices = pd.Series(np.linspace(100, 120, 250) + np.random.normal(0, 2, 250))
score, regime, frame = compute_hso(prices, sma_windows=[10,20,50,100])
frame.to_csv("example_output.csv", index=False)
print(frame.tail())
