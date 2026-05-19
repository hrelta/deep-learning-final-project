# Week 1 Progress Report

**Author:** Elvia Aptanisa
**Week:** 1
**Date:** May 17-23, 2026

---

## What Was Completed This Week

1. Dataset Collection
- Scraped 5,000 user reviews from myBCA app on Google Play Store
- Used google-play-scraper Python library
- Assigned sentiment labels based on star ratings
- Saved dataset as mybca_reviews.csv

2. Exploratory Data Analysis (EDA)
- Analyzed label distribution
- Checked missing values and duplicate entries
- Visualized average review length per sentiment class
- Generated WordCloud for each sentiment class

3. Repository Setup
- Forked project repository from instructor
- Set up folder structure
- Added README.md, data/README.md, requirements.txt
- Uploaded project proposal

---

## EDA Results

| Info | Result |
|---|---|
| Total reviews | 5,000 |
| Missing values | 0 |
| Duplicate reviews | 718 |
| Average review length | 83 characters |

## Label Distribution

| Sentiment | Count | Percentage |
|---|---|---|
| Negative | 2,452 | 49% |
| Positive | 2,104 | 42% |
| Neutral | 444 | 9% |

---

## Key Findings

- Class imbalance confirmed - Neutral class only 9%
- 718 duplicate reviews found - removed in Week 2
- Positive reviews tend to be shorter (avg 6.8 words)
- Negative reviews tend to be longer (avg 18.9 words)

---

## Problems or Blockers

- Initial app ID (com.bca.mybca) was incorrect, returned 404 error
- Fixed by using correct app ID: com.bca.mybca.omni.android

---

## Plan for Next Week

1. Remove 718 duplicate reviews
2. Clean text - remove emojis, symbols, punctuation
3. Normalize text - lowercase, fix abbreviations
4. Remove Bahasa Indonesia stopwords
5. Tokenize reviews
6. Split data 70/15/15
7. Train baseline model - Logistic Regression + TF-IDF
8. Evaluate baseline with Accuracy, F1-Score, Confusion Matrix
