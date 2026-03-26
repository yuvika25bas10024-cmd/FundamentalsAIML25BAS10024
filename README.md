# FundamentalsAIML25BAS10024

**AI Spam Email Detection System**

A lightweight Machine Learning (ML) project that classifies messages as Spam (junk) or Ham (legitimate) using Natural Language Processing (NLP).

**Overview**

This project uses the Multinomial Naive Bayes algorithm to analyze text patterns. It converts raw text into numerical data to predict whether an incoming message is unwanted spam or a safe "ham" email.

**Setup and Installation**

Follow these steps to get the environment ready on your local machine.

**1. Prerequisites**

Python 3.x installed (Check by typing "python --version" or "py --version" in your terminal).

VS Code (or any preferred Code Editor).

**2. Clone/Prepare the Project**

Create a new folder for the project and move your Python script (e.g., spam_detector.py) into it.

**3. Environment Setup and Dependencies**

Open your terminal in the project root folder and run the following command to install the necessary AI libraries:


Windows

py -m pip install pandas scikit-learn


Mac/Linux:

pip3 install pandas scikit-learn

**Configuration**

The system is currently configured with a sample internal dataset for demonstration.

Model: MultinomialNB (Optimized for text frequency data).

Vectorization: CountVectorizer (Converts words into a "Bag of Words" format).

Data Split: 80% Training / 20% Testing.


**How to Run the Project**

Open the project folder in VS Code

Open the terminal (Press Ctrl + `).

Execute the script by running:

py spam_detector.py

**Observe the Output:**

The terminal will display the Accuracy Score.

It will show Predictions for new test cases.

**Expected Output**

When you run the script, you should see a result similar to this:

Accuracy: 0.5

Predictions: ['ham' 'ham']

(Note: Accuracy increases significantly when connected to a larger CSV dataset).

**Project Structure**

spam_detector.py # Main Python logic and ML model

README.md # Project documentation and setup guide


**Screenshots**

<img width="1849" height="832" alt="Screenshot 2026-03-26 181044" src="https://github.com/user-attachments/assets/7d2b1ece-49cf-479e-9fdd-48ae5995d6d1" />
