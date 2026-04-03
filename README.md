# Scam Message Detector

## Overview

A simple web application that classifies text messages as **scam** or **safe** using a machine learning model.
The system combines statistical text classification with basic keyword-based checks for better reliability.

---

## Features

* Classifies messages as scam or safe
* Displays prediction confidence
* Highlights suspicious keywords
* Lightweight and fast (no retraining during runtime)
* Simple UI built with Streamlit

---

## Tech Stack

* Python
* scikit-learn
* pandas
* Streamlit

---

## Project Structure

```
scam-detector/
│── app.py                # Streamlit app
│── model.py              # Training logic
│── train.py              # Runs training and saves model
│── utils.py              # Text preprocessing + helpers
│── data/
│     └── spam.csv        # Dataset
│── model.pkl             # Trained model (generated)
│── vectorizer.pkl        # TF-IDF vectorizer (generated)
│── requirements.txt
│── README.md
│── .gitignore
```

---

## How It Works

1. Text is cleaned (lowercase, remove numbers & punctuation)
2. Converted into numerical form using TF-IDF
3. Classified using Naive Bayes
4. Rule-based keyword check adds an extra validation layer

---

## Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/tushar077-neoo/scam-message-detector.git
cd scam-detector
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Train the model (run once)

```
python train.py
```

### 4. Run the app

```
streamlit run app.py
```

---

## Example

**Input:**

```
You have won a free iPhone! Click here to claim your prize
```

**Output:**

```
Scam detected | Confidence: 0.95
```

---

## Limitations

* Works only on text-based messages
* Accuracy depends on dataset quality
* Rule-based checks are simplistic

---

## Future Improvements

* Improve dataset quality and size
* Add deep learning models
* Build REST API for integration
* Deploy as a web service

---

## License

This project is open-source and available for learning and experimentation.
