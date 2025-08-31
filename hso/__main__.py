import argparse, pandas as pd
from .core import compute_hso, build_public_order
from .weights import EqualWeights, RecencyWeights

def main():
    p = argparse.ArgumentParser(description="HSO open-source CLI (non-proprietary).")
    p.add_argument("--csv", required=True, help="Input CSV file")
    p.add_argument("--col", required=True, help="Price column index or name")
    p.add_argument("--sma", nargs="+", type=int, required=True, help="SMA windows")
    p.add_argument("--recency", action="store_true", help="Use recency weights")
    p.add_argument("--out", default="hso_output.csv", help="Output CSV")
    args = p.parse_args()

    df = pd.read_csv(args.csv)
    if args.col.isdigit():
        price = df.iloc[:, int(args.col)]
    else:
        price = df[args.col]

    n_bits = len(args.sma) + (len(args.sma)*(len(args.sma)-1))//2
    w = RecencyWeights(n_bits).values() if args.recency else EqualWeights(n_bits).values()

    score, regime, frame = compute_hso(price, sma_windows=args.sma, weights=w)
    out = df.copy()
    out["HSO_score"] = frame["score"]
    out["HSO_regime"] = frame["regime"].astype("Int64")
    out.to_csv(args.out, index=False)
    print(f"Wrote {args.out}")

if __name__ == "__main__":
    main()
