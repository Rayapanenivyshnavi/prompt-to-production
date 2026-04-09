skills:
  - name: classify_complaint
    description: Classifies a single complaint row into category, priority, reason, and flag.
    input: A dictionary representing one complaint row with at least a "description" key.
    output: A dictionary with keys: complaint_id, category, priority, reason, flag.
    error_handling: If input is missing description or ambiguous, sets category to "Other" and flag to "NEEDS_REVIEW".

  - name: batch_classify
    description: Reads an input CSV of complaints and applies classify_complaint to each row, writing results to an output CSV.
    input: Path to an input CSV file with complaint rows.
    output: CSV file with classified complaints including complaint_id, category, priority, reason, and flag.
    error_handling: Skips invalid rows, flags ambiguous complaints, and ensures the output CSV is always generated even if some rows fail.