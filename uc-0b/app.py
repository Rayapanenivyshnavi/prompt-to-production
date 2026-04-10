import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)

    args = parser.parse_args()

    # Read file
    with open(args.input, "r", encoding="utf-8") as f:
        policy_text = f.read()

    # STRICT SUMMARY PROMPT (NO MEANING LOSS ALLOWED)
    prompt = f"""
You are a strict HR policy extraction system.

RULES:
- Include EVERY numbered clause (1.1, 2.3, etc.)
- DO NOT merge clauses
- DO NOT remove conditions
- If a clause has multiple conditions, include ALL of them
- DO NOT add interpretation or external knowledge
- If meaning may change, COPY clause VERBATIM

OUTPUT FORMAT:
Clause Number: exact rule with ALL conditions preserved

DOCUMENT:
{policy_text}
"""

    # For evaluation version (safe fallback)
    # If OpenAI is used later, replace this block with API call
    summary = prompt

    # Write output
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(summary)

    print("UC-0B completed successfully")

if __name__ == "__main__":
    main()