skills:
  - name: load_dataset
    description: Reads CSV, validates schema, and reports null actual_spend rows with reasons.
    input: File path (string)
    output: Pandas DataFrame
    error_handling: Raises error if required columns missing; prints null rows before returning.

  - name: compute_growth
    description: Computes month-over-month growth for a given ward and category with formula shown.
    input: Filtered DataFrame (ward + category), growth_type (string)
    output: DataFrame with period, actual_spend, growth, and formula
    error_handling: Returns "NULL" growth if current or previous value is missing; refuses unsupported growth types.