def load_data():
    with open("data/clean_loans.txt", "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines() if line.strip()]


def search(query, data):
    # remove useless words
    stopwords = [
        "what", "is", "the", "for", "a", "an",
        "of", "to", "in", "on", "and", "are"
    ]

    # clean query
    query_words = [
        word for word in query.lower().split()
        if word not in stopwords
    ]

    scored_results = []

    for sentence in data:
        sentence_lower = sentence.lower()
        score = 0

        # keyword matching
        for word in query_words:
            if word in sentence_lower:
                score += 2

        # context understanding 
        if "home" in query.lower() and "home" in sentence_lower:
            score += 3

        if "personal" in query.lower() and "personal" in sentence_lower:
            score += 3

        if "interest" in query.lower() and "interest" in sentence_lower:
            score += 3

        if "tenure" in query.lower() and "tenure" in sentence_lower:
            score += 3

        if "scheme" in query.lower() and "scheme" in sentence_lower:
            score += 3

        if "eligibility" in query.lower() and "eligibility" in sentence_lower:
            score += 3

        # only keep meaningful matches
        if score >= 3:
            scored_results.append((score, sentence.strip()))

    # sort by best match
    scored_results.sort(reverse=True, key=lambda x: x[0])

    # return top 2 best answers
    return [s[1] for s in scored_results[:2]]