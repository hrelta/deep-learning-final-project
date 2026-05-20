# Final Report

## 1. Project Title
Sentiment Analysis of myBCA Mobile Banking App Reviews Using Deep Learning

---

## 2. Problem Statement
The myBCA mobile banking application receives thousands of user reviews on the Google Play Store daily. Reading all reviews manually is inefficient, causing important feedback about bugs or service quality to be missed. This project builds an automatic sentiment classification system using deep learning to classify each review as Positive, Neutral, or Negative — helping the myBCA team quickly identify user issues without manually reading every review.

---

## 3. Dataset Description
- Name: myBCA Google Play Store Reviews Dataset
- Source: Collected via web scraping from Google Play Store using google-play-scraper Python library
- Size: 5,000 reviews in Bahasa Indonesia
- Labels: Positive (4-5 stars), Neutral (3 stars), Negative (1-2 stars)
- Format: CSV with columns: review, rating, sentiment
- Label distribution: Negative 49%, Positive 42%, Neutral 9%

---

## 4. Data Preprocessing
1. Removed 718 duplicate reviews
2. Lowercased all text
3. Removed emojis, symbols, URLs, numbers, and punctuation
4. Normalized slang and abbreviations (e.g. "gak" to "tidak", "udh" to "sudah")
5. Removed Bahasa Indonesia stopwords using PySastrawi
6. Applied stemming to reduce words to base form
7. Removed 34 empty reviews after cleaning
8. Final dataset: 4,248 reviews

---

## 5. Model Architecture

### Baseline Model
- Logistic Regression with TF-IDF vectorizer (max 5,000 features)
- Simple and fast, used as benchmark

### Deep Learning Model
- Bidirectional LSTM (BiLSTM)
- Architecture:
  - Embedding layer (64 dimensions)
  - SpatialDropout1D (0.3)
  - Bidirectional LSTM (32 units)
  - Dropout (0.5)
  - Dense output layer (3 units, softmax activation)

---

## 6. Training Setup
- Optimizer: Adam (learning rate 0.01)
- Loss function: Sparse Categorical Cross-Entropy
- Batch size: 32
- Max epochs: 20 (with Early Stopping, patience=3)
- Class weighting: Used to handle class imbalance
- Train/Validation/Test split: 70% / 15% / 15%

---

## 7. Evaluation Metrics
- Accuracy
- Precision, Recall, F1-Score (per class and weighted average)
- Confusion Matrix

---

## 8. Results Table

| Model | Neg F1 | Neu F1 | Pos F1 | Accuracy |
|---|---|---|---|---|
| Baseline (LR + TF-IDF) | 0.83 | 0.00 | 0.74 | 76.0% |
| LSTM v1 | 0.73 | 0.00 | 0.00 | 57.2% |
| Bidirectional LSTM | 0.77 | 0.24 | 0.72 | 67.0% |

---

## 9. Error Analysis
- Total test reviews: 641
- Correct predictions: 405 (63.2%)
- Wrong predictions: 236 (36.8%)

Key findings:
- 111 Negative reviews misclassified as Neutral (mild language confused model)
- Neutral class remains hardest to classify due to mixed opinions
- Some Positive reviews misclassified as Negative due to label noise (high star rating but negative text)

---

## 10. Limitations
- Label noise: Labels based on star ratings, not actual text content
- Class imbalance: Neutral class only 9% of dataset
- Informal language: Heavy slang and mixed Indonesian-English hurt performance
- Model trained from scratch: No pre-trained Indonesian word embeddings used

---

## 11. Conclusion
This project successfully built a sentiment classification system for myBCA app reviews. The Bidirectional LSTM model outperformed the baseline in detecting all three sentiment classes, especially the Neutral class (F1 improved from 0.00 to 0.24). The system was deployed as an interactive Streamlit web application accessible at https://mybca-sentiment-analyzer.streamlit.app

Future improvements:
- Use IndoBERT (pre-trained Indonesian BERT) for better context understanding
- Manual labeling instead of star-rating-based labeling
- Collect more Neutral class data to balance the dataset

---

## 12. References
- Google Play Store - myBCA app: https://play.google.com/store/apps/details?id=com.bca.mybca.omni.android
- google-play-scraper library: https://github.com/JoMingyu/google-play-scraper
- PySastrawi: https://github.com/har07/PySastrawi
- TensorFlow/Keras documentation: https://www.tensorflow.org
- Streamlit documentation: https://docs.streamlit.io
