import matplotlib.pyplot as plt

def plot_oscillator(df, score_col="score", date_index=True):
    plt.figure(figsize=(8,3))
    y = df[score_col].dropna()
    x = y.index if date_index else range(len(y))
    plt.plot(x, y, label="HSO")
    plt.axhline(0, linestyle="--", linewidth=0.8)
    plt.axhline(0.5, linestyle="--", linewidth=0.8)
    plt.axhline(-0.5, linestyle="--", linewidth=0.8)
    plt.title("Health Score Oscillator")
    plt.ylabel("Score")
    plt.xlabel("Date" if date_index else "Index")
    plt.legend()
    plt.tight_layout()
    return plt.gcf()
