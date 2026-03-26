from rag import load_data, search

print("🏦 Bank of Maharashtra Loan Assistant")
print("Ask anything about loans (interest, tenure, eligibility, etc.)")
print("Type 'exit' to quit\n")

data = load_data()

while True:
    query = input("Ask your question: ")

    if query.lower() == "exit":
        print("Goodbye 👋")
        break

    results = search(query, data)

    if results:
        print("\n💡 Answer:\n")

        # combine results into one clean answer
        answer = " ".join(results)
        answer = answer.replace("  ", " ").strip().capitalize()

        # contextual response
        if "interest" in query.lower():
            print(f"The interest rate information is as follows:\n{answer}")

        elif "tenure" in query.lower():
            print(f"The loan tenure details are:\n{answer}")

        elif "eligibility" in query.lower():
            print(f"The eligibility criteria include:\n{answer}")

        elif "scheme" in query.lower():
            print(f"Here are the details about the scheme:\n{answer}")

        else:
            print(answer)

    else:
        print("❌ Sorry, I couldn’t find relevant loan information. Try rephrasing your question.")