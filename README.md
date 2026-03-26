# Bank-loan-assistant
Lightweight AI-powered loan assistant using web scraping and retrieval-based search.

# Bank of Maharashtra Loan Assistant

## Project Overview

This project is a lightweight AI-powered Loan Product Assistant built as part of a technical assessment.

The assistant is designed to answer user queries related to **Bank of Maharashtra loan products**, such as:
- Home Loans
- Personal Loans
- Salary-based Loans

It uses a **retrieval-based approach** to extract relevant information from the bank’s official website and provide accurate responses.

---

## Objective

To build a system that:
- Scrapes loan-related data from official sources
- Cleans and structures the data
- Retrieves relevant information based on user queries
- Provides clear and contextual answers

---


---

## Technologies Used

- Python
- BeautifulSoup (Web Scraping)
- Requests (HTTP Handling)
- Regular Expressions (Data Cleaning)

---


---

## Workflow Explanation

### 1. Data Scraping
- Extracted loan-related content from:
  - Home Loan page
  - Personal Loan page
  - Salary Loan page
- Removed scripts, styles, and unnecessary HTML elements

---

### 2. Data Cleaning & Processing
- Removed navigation elements and irrelevant text
- Filtered content using domain-specific keywords:
  - interest rate
  - tenure
  - eligibility
  - loan schemes
- Split data into smaller meaningful chunks for better retrieval

---

### 3. Retrieval System (Lightweight RAG)
- Implemented a keyword-based scoring system
- Removed stopwords from user queries
- Added **context-aware scoring**, such as:
  - Home vs Personal Loan
  - Interest vs Tenure vs Eligibility
- Ranked results based on relevance score

---

### 4. Answer Generation
- Combined top results into a clean response
- Added contextual formatting based on query type:
  - Interest rate queries
  - Tenure queries
  - Scheme-related queries

---

## Key Features

- Lightweight (No heavy ML models required)
- Fast and efficient retrieval
- Context-aware query handling
- Clean and readable responses
- Robust data cleaning pipeline

---

## Challenges Faced

### 1. Noisy Web Data
- The scraped data contained navigation menus and irrelevant content  
✅ Solved by filtering using keywords and removing UI elements

### 2. Poor Initial Retrieval Quality
- Initial results were too generic and repetitive  
✅ Solved by implementing a scoring-based ranking system

### 3. Lack of Query Understanding
- System couldn’t differentiate between loan types  
✅ Solved using context-aware boosting logic

---

## Potential Improvements

- Integrate vector search (FAISS) for semantic retrieval
- Use LLM (OpenAI / Ollama) for more natural responses
- Build a web interface (Streamlit / React)
- Add structured JSON knowledge base
- Improve entity recognition (loan types, schemes)

---
### Example Questions
- What is the interest rate for home loan?
- What is the tenure for personal loan?
- What are eligibility criteria?
