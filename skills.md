skills:
  - name: load_dataset
    description: Reads CSV, validates columns, reports null count and rows before returning.
    input: Path to CSV file.
    output: Pandas DataFrame with validation report.
    error_handling: Raises error if columns missing; flags and reports nulls.

  - name: compute_growth
    description: Computes growth (MoM, YoY) for given ward + category.
    input: DataFrame, ward name, category name, growth_type.
    output: Table with period, actual_spend, formula, growth value.
    error_handling: Refuses if growth_type not provided; skips rows with null actual_spend and reports reason.
