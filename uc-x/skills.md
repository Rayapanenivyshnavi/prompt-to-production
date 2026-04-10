skills:
  - name: retrieve_documents
    description: Loads and indexes policy documents
    input: question (string)
    output: relevant policy text with section reference
    error_handling: returns empty if no match found

  - name: answer_question
    description: Answers using only one policy source
    input: question + retrieved text
    output: formatted answer OR refusal message
    error_handling: returns refusal if no exact match found