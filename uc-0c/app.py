import argparse
import pandas as pd

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--ward", required=True)
    parser.add_argument("--category", required=True)
    parser.add_argument("--growth-type", required=True)

    args = parser.parse_args()

    if args.growth_type != "MoM":
        raise ValueError("Only MoM allowed")

    df = pd.read_csv(args.input)

    df = df[(df["ward"] == args.ward) & (df["category"] == args.category)]

    df["is_null"] = df["actual_spend"].isna()

    df = df.sort_values("period")

    df["mom_growth"] = df["actual_spend"].pct_change() * 100

    df["formula"] = "(current - previous) / previous * 100"

    df.to_csv(args.output, index=False)

    print("UC-0C completed successfully")

if __name__ == "__main__":
    main()