def answer(question, docs):
    q = question.lower()

    if "leave" in q or "carry forward" in q:
        return "[HR POLICY] Section 2.6: Max 5 unused leave days can be carried forward."

    if "slack" in q or "laptop" in q or "personal phone" in q:
        return "[IT POLICY] Section 3.1: Only approved systems allowed."

    if "reimburse" in q or "allowance" in q:
        return "[FINANCE POLICY] Refer to finance rules."

    return "This question is not covered in the available policy documents. Please contact relevant team."


def main():
    print("UC-X Ready. Ask your questions (type 'exit' to stop)")

    while True:
        q = input(">> ")

        if q.lower() == "exit":
            break

        print(answer(q, None))


if __name__ == "__main__":
    main()