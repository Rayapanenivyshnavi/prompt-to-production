import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)

    args = parser.parse_args()

    # Read input file
    with open(args.input, "r", encoding="utf-8") as f:
        policy_text = f.read()

    # 🔥 YOUR PROMPT (IMPORTANT)
    prompt = f"""
Summarize the following policy document.

Rules:
1. Include ALL numbered clauses
2. Do NOT drop any conditions
3. Keep words like 'must', 'requires', 'not permitted'
4. Do NOT add extra information
5. If meaning is lost, copy exact clause
6. Mention clause numbers

Document:
{policy_text}
"""

    # For now, just write prompt as output (dummy)
    summary = prompt   # later replace with AI response

    # Write output file
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(summary)

if __name__ == "__main__":
    main()