import re
import os

# create folder if needed
os.makedirs("data", exist_ok=True)

# read raw data
with open("data/raw/loans.txt", "r", encoding="utf-8") as f:
    text = f.read()

# keep line structure but clean spaces
text = re.sub(r"[ \t]+", " ", text)

# splits into small chunks
chunks = re.split(r"[.\n•]", text)

keywords = [
    "interest", "rate", "loan", "tenure",
    "eligibility", "processing", "amount",
    "repayment", "emi", "limit"
]

bad_words = [
    "home", "about us", "contact", "skip to content",
    "menu", "login", "register", "privacy", "policy",
    "copyright", "all rights reserved"
]

filtered = []

for chunk in chunks:
    chunk = chunk.strip()

    if len(chunk) < 40:
        continue

    if any(k in chunk.lower() for k in keywords):
        if not any(bad in chunk.lower() for bad in bad_words):
            filtered.append(chunk)

# remove duplicates
clean_data = list(set(filtered))

# WRITE LINE BY LINE 
with open("data/clean_loans.txt", "w", encoding="utf-8") as f:
    for line in clean_data:
        f.write(line + "\n")

print("✅ Clean data properly structured now!")