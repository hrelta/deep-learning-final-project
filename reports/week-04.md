# Week 4 Progress Report

**Author:** Elvia Aptanisa
**Week:** 4
**Date:** May 20-23, 2026

---

## What Was Completed This Week

1. Error Analysis
- Analyzed 641 test set reviews
- Identified 236 misclassified reviews (36.8%)
- Found key patterns in model mistakes
- Visualized misclassification per class

2. Streamlit App (In Progress)
- Building interactive sentiment analyzer app
- Users can input myBCA review text and get prediction

---

## Error Analysis Results

| Metric | Result |
|---|---|
| Total test reviews | 641 |
| Correct predictions | 405 (63.2%) |
| Wrong predictions | 236 (36.8%) |

**Misclassification breakdown:**

| Actual | Predicted | Count |
|---|---|---|
| Negative | Neutral | 111 |
| Negative | Positive | 16 |
| Neutral | Negative | 30 |
| Neutral | Positive | 8 |

---

## Key Findings

1. Label Noise - Some reviews have misleading labels based on star ratings
2. Ambiguous Negative Reviews - Many negative reviews use polite language
3. Neutral Class Difficulty - Neutral reviews contain mixed opinions
4. Informal Language - Slang and mixed language hurt model performance

---

## Problems or Blockers

- BiLSTM model needs to be retrained each session (model file lost after Colab session ends)
- Neutral class still underperforming due to class imbalance

---

## Plan to Complete

1. Finish Streamlit app
2. Write final report
3. Prepare presentation slides
