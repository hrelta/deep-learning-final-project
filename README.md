# Sentiment Analysis of myBCA Mobile Banking App Reviews

**Author:** Elvia Aptanisa  
**Course:** Introduction to Deep Learning - Narxoz University Kazakhstan  
**Type:** Individual Project  

---

## Project Overview

This project builds an automatic sentiment classification system for user reviews 
of the myBCA mobile banking application from the Google Play Store. 
The model classifies each review into three categories - Positive, Neutral, or 
Negative - using a deep learning approach with LSTM (Long Short-Term Memory).

---

## Live Demo

Try the app here: https://mybca-sentiment-analyzer.streamlit.app
---

## Repository Structure

```
C:.
│   final-report.md
│   project-proposal.md
│   proposal_elvia.pdf
│   README.md
│   requirements.txt
│
├───data
│       README.md
│
├───notebooks
│       week01_data_collection.ipynb
│       week01_eda.ipynb
│       week02_preprocessing.ipynb
│
├───reports
│       week-01.md
│       week-02.md
│
├───results
│       baseline_confusion_matrix.png
│       eda_label_distribution.png
│       eda_review_length.png
│       eda_wordcloud.png
│
└───src
```
---

## Dataset

- Source: Google Play Store - myBCA app reviews
- Collection method: Web scraping using google-play-scraper
- Size: 5,000 reviews in Bahasa Indonesia
- Labels: Positive (4-5 stars), Neutral (3 stars), Negative (1-2 stars)

---

## Weekly Progress

| Week | Status | Focus |
|---|---|---|
| Week 1 | Done | Data collection, EDA, repository setup |
| Week 2 | Done | Preprocessing, baseline model |
| Week 3 | Done | LSTM model training |
| Week 4 | Done | Error analysis, Streamlit app, final report |
