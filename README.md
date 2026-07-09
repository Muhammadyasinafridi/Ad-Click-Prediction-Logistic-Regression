# Ad-Click-Prediction-Logistic-Regression
Machine learning model using Logistic Regression to predict e-commerce ad click-through rates based on user session metrics and demographic data. Built with Python &amp; Streamlit
# 🎯 E-Commerce Ad Click Predictor

An end-to-end Machine Learning web application built to predict consumer ad-click behavior using session metrics and demographic data. Powered by a **Logistic Regression** classification model and deployed via **Streamlit**.

---

## 📌 Features

* **Interactive Interface:** Clean, user-friendly web UI built with Streamlit.
* **Real-time Predictions:** Input session parameters and get instant predictions on whether a user is likely to click an ad.
* **Machine Learning Model:** Binary classification using Logistic Regression optimized for session-based engagement prediction.

---

## 📊 Dataset Features & Key Metrics

The model evaluates consumer behavior using key indicators:

| Feature | Description |
| :--- | :--- |
| **Daily Time Spent on Site** | Consumer time on site in minutes |
| **Age** | Customer age in years |
| **Area Income** | Avg. income of the geographical area of consumer |
| **Daily Internet Usage** | Avg. minutes per day consumer is on the internet |
| **Clicked on Ad** | Target Variable (0 = Did not click, 1 = Clicked) |

---

## 🛠️ Tech Stack

* **Language:** Python
* **Machine Learning:** `scikit-learn`
* **Data Manipulation & Analysis:** `pandas`, `numpy`
* **Web Framework:** `Streamlit`
* **Deployment:** Streamlit Community Cloud

---

## 🚀 Quickstart & Local Installation

To run this app locally on your machine, follow these steps:

### 1. Clone the repository
```bash
git clone [https://github.com/YOUR_GITHUB_USERNAME/ad-click-predictor.git](https://github.com/YOUR_GITHUB_USERNAME/ad-click-predictor.git)
cd ad-click-predictor
