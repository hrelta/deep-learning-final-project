import streamlit as st
import numpy as np
import re
import string
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import pickle

st.set_page_config(page_title="myBCA Sentiment Analyzer", layout="centered")

st.title("myBCA Review Sentiment Analyzer")
st.markdown("Analyze the sentiment of myBCA mobile banking app reviews.")
st.markdown("---")

@st.cache_resource
def load_everything():
    df = pd.read_csv("data/mybca_reviews.csv")
    df = df.drop_duplicates(subset='review', keep='first')

    def clean_text(text):
        text = str(text).lower()
        text = text.encode('ascii', 'ignore').decode('ascii')
        text = re.sub(r'http\S+|www\S+', '', text)
        text = re.sub(r'\d+', '', text)
        text = text.translate(str.maketrans('', '', string.punctuation))
        text = re.sub(r'\s+', ' ', text).strip()
        return text

    df['review_clean'] = df['review'].apply(clean_text)
    df = df[df['review_clean'].str.strip() != '']

    tfidf = TfidfVectorizer(max_features=5000)
    X = tfidf.fit_transform(df['review_clean'])

    le = LabelEncoder()
    y = le.fit_transform(df['sentiment'])

    model = LogisticRegression(max_iter=1000, random_state=42)
    model.fit(X, y)

    return model, tfidf, le

model, tfidf, le = load_everything()

def predict_sentiment(text):
    def clean_text(text):
        text = str(text).lower()
        text = text.encode('ascii', 'ignore').decode('ascii')
        text = re.sub(r'http\S+|www\S+', '', text)
        text = re.sub(r'\d+', '', text)
        text = text.translate(str.maketrans('', '', string.punctuation))
        text = re.sub(r'\s+', ' ', text).strip()
        return text

    cleaned = clean_text(text)
    vec = tfidf.transform([cleaned])
    pred_class = model.predict(vec)[0]
    pred_prob = model.predict_proba(vec)[0]
    label = le.inverse_transform([pred_class])[0]
    confidence = pred_prob[pred_class] * 100
    return label, confidence, pred_prob

st.subheader("Enter a myBCA Review")
review_input = st.text_area(
    "Type or paste a review here:",
    placeholder="Contoh: Aplikasi sangat mudah digunakan dan cepat...",
    height=120
)

if st.button("Analyze Sentiment", use_container_width=True):
    if review_input.strip() == "":
        st.warning("Please enter a review first!")
    else:
        with st.spinner("Analyzing..."):
            label, confidence, probs = predict_sentiment(review_input)

        if label == "Positive":
            st.success(f"Sentiment: {label} ({confidence:.1f}% confidence)")
        elif label == "Negative":
            st.error(f"Sentiment: {label} ({confidence:.1f}% confidence)")
        else:
            st.info(f"Sentiment: {label} ({confidence:.1f}% confidence)")

        st.markdown("**Probability breakdown:**")
        for i, cls in enumerate(le.classes_):
            st.progress(float(probs[i]), text=f"{cls}: {probs[i]*100:.1f}%")

st.markdown("---")
st.markdown("*Built by Elvia Aptanisa - Introduction to Deep Learning, Narxoz University Kazakhstan*")
