skills:
  - name: retrieve_policy
    description: Loads a .txt policy file and returns its content as structured, numbered sections.
    input: Path to the .txt policy file (String).
    output: A list or dictionary of structured sections with clause numbers and text.
    error_handling: Raise an error if the file cannot be found or read. If unnumbered text is found, flag it as 'Uncategorized'.

  - name: summarize_policy
    description: Takes structured policy sections and produces a compliant summary with clause references, ensuring no conditions are dropped.
    input: Structured sections from retrieve_policy.
    output: A multi-line string containing the compliant summary with all numbered clauses.
    error_handling: If a clause's meaning might be altered during summarization, output the clause verbatim with a flag.
