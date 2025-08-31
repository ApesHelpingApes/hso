import numpy as np

class EqualWeights:
    def __init__(self, n_bits: int):
        self.w = np.ones(n_bits)/n_bits
    def values(self):
        return self.w

class RecencyWeights:
    """Heavier weight to earlier bits (assuming you order short-term first)."""
    def __init__(self, n_bits: int, decay: float = 0.9):
        v = np.array([decay**i for i in range(n_bits)], dtype=float)
        self.w = v/np.sum(v)
    def values(self):
        return self.w
