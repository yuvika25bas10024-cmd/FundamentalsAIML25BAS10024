# FundamentalsAIML25BAS10024

**Project Report: AI-Powered Spam Email Detection System**


**1. Introduction**

The objective of this project is to develop a Machine Learning (ML) system capable of automatically classifying electronic messages as Spam (unsolicited/junk) or Ham (legitimate). This is a classic "Binary Classification" problem in the field of Natural Language Processing (NLP).

**2. Methodology**

The system follows a standard data science pipeline:
Data Collection: Gathering a labeled dataset of emails.
Preprocessing: Cleaning the text and removing noise.
Feature Extraction (Vectorization): Converting raw text into numerical data using CountVectorizer (Bag of Words).
Model Training: Using the Multinomial Naive Bayes algorithm, which is mathematically optimized for text frequency data.
Evaluation: Testing the model on unseen data to check for accuracy.

**3. System Architecture**

The code uses a modular approach:
Input Layer: Raw text strings (emails).
Processing Layer:
pandas for data handling.
scikit-learn for splitting data and vectorization.
Model Layer: The Naive Bayes classifier calculates the probability of a message being spam based on the occurrence of specific keywords.
Output Layer: A prediction label ("Spam" or "Ham").

**4. Implementation Details**

Language: Python 3.14
Libraries:
Pandas: For data manipulation and structuring.
Scikit-Learn: For the Machine Learning algorithm and evaluation metrics.
Algorithm: Multinomial Naive Bayes.

**5. Results & Discussion**

During initial testing with a sample dataset:
Training/Test Split: 80% Training, 20% Testing.
Performance: The model successfully identified basic patterns (e.g., words like "Free" or "Win" often correlate with Spam).
Limitation: With a very small dataset (6 rows), accuracy remains low. To achieve industry-standard accuracy (>95%), a larger dataset like the UCI SMS Spam Collection is required.
6. Conclusion
The project demonstrates that even a simple Naive Bayes model can effectively filter messages. By scaling the dataset and using advanced techniques like TF-IDF (Term Frequency-Inverse Document Frequency), the system can become a robust tool for enhancing email security and user experience.

**Screenshots**

<img width="1849" height="832" alt="Screenshot 2026-03-26 181044" src="https://github.com/user-attachments/assets/7d2b1ece-49cf-479e-9fdd-48ae5995d6d1" />
