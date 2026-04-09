import argparse
import pandas as pd

def load_dataset(path):
    df = pd.read_csv(path)
    # Validate columns
    required = ["period","ward","category","budgeted_amount","actual_spend","notes"]
    for col in required:
        if col not in df.columns:
            raise ValueError(f"Missing column: {col}")
    # Report nulls
    nulls = df[df["actual_spend"].isnull()]
    if not nulls.empty:
        print("Null rows found:")
        print(nulls[["period","ward","category","notes"]])
    return df

def compute_growth(df, ward, category, growth_type):
    if growth_type != "MoM":
        raise ValueError("Growth type must be specified and supported (MoM only).")
    subset = df[(df["ward"]==ward) & (df["category"]==category)].copy()
    subset["actual_spend"] = pd.to_numeric(subset["actual_spend"], errors="coerce")
    subset["MoM_growth"] = subset["actual_spend"].pct_change() * 100
    subset["formula"] = "(current - previous)/previous * 100"
    return subset

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--ward", required=True)
    parser.add_argument("--category", required=True)
    parser.add_argument("--growth-type", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    df = load_dataset(args.input)
    result = compute_growth(df, args.ward, args.category, args.growth_type)
    result.to_csv(args.output, index=False)

if __name__ == "__main__":
    main()
