# Intelligent Job Recommender

An end-to-end machine learning & NLP project that analyzes PDF resumes to predict the candidate’s job profile using a KNN classifier, then dynamically scrapes LinkedIn to recommend real-time job openings based on the detected profile and chosen location.

✨ Features

✅ Resume Parsing & Cleaning

    Reads PDF resumes and extracts text using PyPDF2.

    Cleans the text by removing URLs, mentions, emojis, and non-ASCII characters with regex and NLTK.

✅ Profile Prediction with KNN

    Converts the cleaned text into TF-IDF vectors.

    Uses a K-Nearest Neighbors (KNN) classifier to predict the most likely job category.

✅ Real-time Job Recommendations

    Scrapes LinkedIn job postings based on the predicted profile and location.

✅ Interactive Streamlit Interface

    Upload your resume, select your location, and instantly get tailored job listings.

🖥️ Demo
<img src="app.png" alt="App Screenshot" />


⚙️ Tech Stack

    Python for all data processing & backend.

    NLTK for text cleaning and stopword management.

    Scikit-learn for TF-IDF vectorization and job category classification.

    BeautifulSoup & Requests for web scraping LinkedIn job listings.

    PyPDF2 for reading PDF resumes.

    Streamlit for the interactive user interface.

    Pandas for data handling and display.

📂 Model & Vectorizer

🚀 Usage

Run the Streamlit app: streamlit run app.py

Then:

    Upload your resume as a PDF.

    Type the country or city where you want to find jobs.

    Get your predicted profile and see matching job listings fetched live from LinkedIn.

🔍 Example Predicted Profiles

    Data Scientist

    Java Developer

    Business Analyst

    Python Developer

    DevOps Engineer
