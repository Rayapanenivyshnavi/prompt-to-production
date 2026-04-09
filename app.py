def retrieve_documents(files):
    docs = {}
    for f in files:
        with open(f, 'r', encoding='utf-8') as file:
            docs[f] = file.read()
    return docs

def answer_question(question, docs):
    # For now, always return refusal template
    return "This question is not covered in the available policy documents (policy_hr_leave.txt, policy_it_acceptable_use.txt, policy_finance_reimbursement.txt). Please contact [relevant team] for guidance."

def main():
    docs = retrieve_documents([
        "../data/policy-documents/policy_hr_leave.txt",
        "../data/policy-documents/policy_it_acceptable_use.txt",
        "../data/policy-documents/policy_finance_reimbursement.txt"
    ])
    
    print("Type 'exit' to quit.")
    while True:
        q = input("Question: ")
        if q.lower() == "exit":
            break
        print("Answer:", answer_question(q, docs))

if __name__ == "__main__":
    main()