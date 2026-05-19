# Dataset Instructions

The raw dataset is not uploaded to this repository.
To reproduce the dataset, follow the steps below.

---

## Dataset Information

| Info | Details |
|---|---|
| App Name | myBCA: BCA Banking Apps |
| Developer | PT Bank Central Asia Tbk. |
| Source | Google Play Store |
| App ID | com.bca.mybca.omni.android |
| Language | Bahasa Indonesia |
| Size | 5,000 reviews |
| Format | CSV |

---

## How to Reproduce the Dataset

Step 1 - Install the scraping library

pip install google-play-scraper

Step 2 - Run the scraping notebook

Open notebooks/week01_data_collection.ipynb in Google Colab and run all cells.

---

## Dataset Columns

| Column | Description |
|---|---|
| review | Text written by the user |
| rating | Original star rating (1-5) |
| sentiment | Assigned label (Positive, Neutral, Negative) |
