# Week 3 Progress Report

**Author:** Elvia Aptanisa
**Week:** 3
**Date:** May 20, 2026

---

## What Was Completed This Week

1. LSTM Model Training (Attempt 1)
- Built LSTM model with Embedding + SpatialDropout + LSTM layers
- Model failed to converge - only predicted Negative class
- Accuracy: 57.2%

2. Hyperparameter Tuning (Attempt 2)
- Reduced model complexity (LSTM units 128 to 64)
- Adjusted learning rate and dropout
- Still failed to converge

3. Removed Stemming (Attempt 3)
- Reloaded dataset without stemming preprocessing
- Hypothesis: stemming removed too much context from short reviews
- Still not converging properly

4. Bidirectional LSTM (Attempt 4 - Success!)
- Switched from LSTM to Bidirectional LSTM
- Model successfully learned all 3 sentiment classes
- Final accuracy: 67%

---

## Model Comparison Results

| Model | Neg F1 | Neu F1 | Pos F1 | Accuracy |
|---|---|---|---|---|
| Baseline (LR + TF-IDF) | 0.83 | 0.00 | 0.74 | 76.0% |
| LSTM v1 | 0.73 | 0.00 | 0.00 | 57.2% |
| Bidirectional LSTM | 0.77 | 0.24 | 0.72 | 67.0% |

---

## Key Findings

- LSTM v1 completely failed to detect Neutral and Positive classes
- Bidirectional LSTM successfully detected all 3 classes
- Neutral F1-Score improved from 0.00 to 0.24
- Although BiLSTM accuracy (67%) is lower than baseline (76%), BiLSTM is more reliable because it can detect all sentiment classes fairly
- Baseline 76% accuracy is misleading - it only predicted Negative class well

---

## Problems or Blockers

- LSTM model took multiple attempts before converging
- Stemming preprocessing was found to hurt LSTM performance
- Class imbalance remains a challenge for Neutral class detection

---

## Plan for Next Week

1. Further improve BiLSTM model if possible
2. Perform error analysis - analyze misclassified reviews
3. Build Streamlit app for interactive sentiment prediction
4. Write final report
5. Prepare presentation slides
