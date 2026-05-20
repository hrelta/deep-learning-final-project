import streamlit as st
import numpy as np
import re
import string
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
import pandas as pd

st.set_page_config(
    page_title="myBCA Sentiment Analyzer",
    layout="centered"
)

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

    tokenizer = Tokenizer(num_words=10000, oov_token='<OOV>')
    tokenizer.fit_on_texts(df['review_clean'])

    le = LabelEncoder()
    le.fit(df['sentiment'])

    model = load_model("bilstm_sentiment_model.keras")

    return model, tokenizer, le

model, tokenizer, le = load_everything()

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
    seq = tokenizer.texts_to_sequences([cleaned])
    padded = pad_sequences(seq, maxlen=100, padding='post', truncating='post')
    pred_prob = model.predict(padded, verbose=0)
    pred_class = np.argmax(pred_prob, axis=1)[0]
    label = le.inverse_transform([pred_class])[0]
    confidence = pred_prob[0][pred_class] * 100
    return label, confidence, pred_prob[0]

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
        classes = le.classes_
        for i, cls in enumerate(classes):
            st.progress(float(probs[i]), text=f"{cls}: {probs[i]*100:.1f}%")

st.markdown("---")
st.markdown("*Built by Elvia Aptanisa - Introduction to Deep Learning, Narxoz University Kazakhstan*")
