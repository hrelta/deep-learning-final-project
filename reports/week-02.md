# Week 2 Progress Report

**Author:** Elvia Aptanisa
**Week:** 2
**Date:** May 20, 2026

---

## What Was Completed This Week

1. Text Preprocessing
- Removed 718 duplicate reviews
- Cleaned text: removed emojis, symbols, URLs, punctuation, numbers
- Normalized text: fixed common abbreviations and slang words
- Removed Bahasa Indonesia stopwords using PySastrawi
- Applied stemming to reduce words to their base form
- Removed 34 empty reviews after cleaning
- Final cleaned dataset: 4,248 reviews

2. Train/Validation/Test Split
- Training set: 2,998 reviews (70%)
- Validation set: 641 reviews (15%)
- Test set: 643 reviews (15%)

3. Baseline Model - Logistic Regression + TF-IDF
- Trained Logistic Regression with TF-IDF vectorizer (max 5,000 features)
- Evaluated on test set

---

## Results

| Class | Precision | Recall | F1-Score |
|---|---|---|---|
| Negative | 0.75 | 0.93 | 0.83 |
| Neutral | 0.00 | 0.00 | 0.00 |
| Positive | 0.79 | 0.69 | 0.74 |
| Accuracy | | | 0.76 |

---

## Key Findings

- Baseline accuracy: 76%
- Neutral class F1-Score is 0.00 - model completely failed to detect neutral reviews
- This confirms the class imbalance challenge mentioned in the proposal
- LSTM model is expected to perform better, especially for the Neutral class

---

## Problems or Blockers

- 34 reviews became empty after cleaning (contained only emojis or symbols)
- These were removed before saving the final cleaned dataset
- No other major blockers this week

---

## Plan for Next Week

1. Build LSTM model with word embeddings
2. Handle class imbalance using class weighting
3. Train LSTM and compare results with baseline
4. Plot training and validation loss curves
5. Evaluate with Accuracy, F1-Score, and Confusion Matrix
