import streamlit as st
import pickle
import re
import nltk
import PyPDF2

import requests
from bs4 import BeautifulSoup
import pandas as pd

nltk.download('punkt')
nltk.download('stopwords')

clf = pickle.load(open('model.pkl','rb'))
tfidfd = pickle.load(open('tfidf.pkl','rb'))

def clean_resume(resume_text):
    clean_text = re.sub('http\S+\s*', ' ', resume_text)
    clean_text = re.sub('RT|cc', ' ', clean_text)
    clean_text = re.sub('#\S+', '', clean_text)
    clean_text = re.sub('@\S+', '  ', clean_text)
    clean_text = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', clean_text)
    clean_text = re.sub(r'[^\x00-\x7f]', r' ', clean_text)
    clean_text = re.sub('\s+', ' ', clean_text)
    return clean_text

def get_url(job,loc):
    job=job.strip()
    job=job.replace(" ","+")
    url=f"https://www.linkedin.com/jobs/search?keywords={job}&location={loc}"
    return url

def get_record(card):
    job_title=card.find('h3','base-search-card__title').text.strip()
    job_date=card.find('time').get('datetime')
    job_url=card.find('a','hidden-nested-link').get("href")
    job_loc = card.find('span', {'class': 'job-search-card__location'}).text.strip()
    record = (job_title,job_date,job_loc,  job_url)
    return record

def get_data(cards):
    records = []
    for card in cards:
        record = get_record(card)
        records.append(record)
    columns = [
        'job_title',
        'job_date',
        'job_loc',
        'job_url']
    df = pd.DataFrame(data=records, columns=columns)
    df = df.sort_values(by='job_date', ascending=False)
    return df
def main():
    st.title("Job Recommandation")
    uploaded_file = st.file_uploader('Upload Resume', type=['pdf'])

    if uploaded_file is not None:
        resume_text  = ""
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            resume_text  += page.extract_text()
        cleaned_resume = clean_resume(resume_text)
        input_features = tfidfd.transform([cleaned_resume])
        prediction_id = clf.predict(input_features)[0]

        category_mapping = {
            15: "Java Developer",
            23: "Testing",
            8: "DevOps Engineer",
            20: "Python Developer",
            24: "Web Designing",
            12: "HR",
            13: "Hadoop",
            3: "Blockchain",
            10: "ETL Developer",
            18: "Operations Manager",
            6: "Data Science",
            22: "Sales",
            16: "Mechanical Engineer",
            1: "Arts",
            7: "Database",
            11: "Electrical Engineering",
            14: "Health and fitness",
            19: "PMO",
            4: "Business Analyst",
            9: "DotNet Developer",
            2: "Automation Testing",
            17: "Network Security Engineer",
            21: "SAP Developer",
            5: "Civil Engineer",
            0: "Advocate",
        }

        category_name = category_mapping.get(prediction_id, "Unknown")
        url = get_url(category_name)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        cards = soup.find_all('div', 'base-search-card__info')
        df=get_data(cards)
        df = df.reset_index(drop=True)
        st.write("Profile:", category_name)
        with st.expander("Similar Profiles"):
            st.write(df)






# python main
if __name__ == "__main__":
    main()