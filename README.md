# 🛡️ SpamGuard AI — Intelligent Email Spam & Phishing Detector

An end-to-end Machine Learning web application designed to classify emails as **Spam** or **Ham (Legitimate)** in real-time. Built with a custom NLP preprocessing pipeline, Scikit-Learn **Logistic Regression**, a **FastAPI** backend, and a modern **Tailwind CSS** glassmorphic interface.

🔗 **Live Demo:** [https://spam-email-classifier-dkwt.onrender.com/](https://spam-email-classifier-dkwt.onrender.com/)

---

## 📸 Key Features

- **⚡ Real-Time Classification:** Instant inference classifying incoming emails as Spam or Clean Ham.
- **🧹 End-to-End NLP Preprocessing:**
  - Case folding (lowercase conversion)
  - Punctuation & numeric filtering
  - Emoji detection and stripping
  - Stopword filtering using NLTK
  - Text vectorization with Scikit-Learn
- **🎨 Glassmorphic Modern UI:** Dark-mode interface crafted with Tailwind CSS v3, featuring ambient glows, animated status indicators, and responsive grid layouts.
- **🧪 One-Click Test Presets:** Built-in test samples (Bank Phishing, Crypto Lottery, Work Meeting, and Personal Note) for quick evaluation.
- **🔍 Token & Metric Insights:** Displays analysis latency (in ms), token count, and highlighted trigger keywords.
- **🚀 Production-Ready REST API:** Fast, lightweight asynchronous endpoints powered by FastAPI.

---

## 🛠️ Tech Stack

| Layer | Technologies |
| :--- | :--- |
| **Machine Learning** | Scikit-Learn (`LogisticRegression`, `CountVectorizer`), NLTK, Pandas, NumPy, Joblib |
| **Backend Framework** | FastAPI, Uvicorn, Pydantic |
| **Frontend** | HTML5, Tailwind CSS v3, Vanilla JavaScript |
| **Deployment** | Render (Web Service) |

---

## 📁 Project Structure

```text
Spam Email/
├── data/
│   └── spam.csv                  # Email dataset
├── preprocessing/
│   ├── clean_text.py             # Custom NLP cleaning functions
│   ├── eda.ipynb                 # EDA, model training & hyperparameter tuning
│   └── Spam_Model.pkl            # Serialized trained model pipeline
├── index.html                    # Tailwind CSS dark-mode web application
├── main.py                       # FastAPI application & route handlers
├── requirements.txt              # Production Python dependencies
├── .gitignore                    # Git ignore configurations
└── README.md                     # Project documentation
```

---

## 🔌 API Reference

### 1. Health Check
Checks if the backend and ML model are ready.

- **URL:** `/health`
- **Method:** `GET`
- **Response:**
  ```json
  {
    "status": "ok"
  }
  ```

---

### 2. Predict Email
Classifies an email string as spam or ham.

- **URL:** `/predict`
- **Method:** `POST`
- **Headers:** `Content-Type: application/json`
- **Request Body:**
  ```json
  {
    "email": "Subject: URGENT! Your bank account is suspended. Click here to verify your password."
  }
  ```
- **Response:**
  ```json
  {
    "prediction": 1,
    "is_spam": true
  }
  ```
  *(Where `1` = Spam, `0` = Ham)*

---

## 💻 Local Setup & Development

Follow these steps to run the project locally on your machine:

### 1. Clone the Repository
```bash
git clone https://github.com/bhumitsingh856-cyber/spam-email-classifier.git
cd "Spam Email"
```

### 2. Create and Activate a Virtual Environment

**Windows:**
```powershell
python -m venv venv
.\venv\Scripts\activate
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
uvicorn main:app --reload --port 3000
```

Open your browser and navigate to:
```text
http://localhost:3000/
```

---

## 🚀 Deployment (Render)

This project is configured to deploy directly to **Render** as a Python Web Service:

1. **Build Command:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Start Command:**
   ```bash
   uvicorn main:app --host 0.0.0.0 --port $PORT
   ```
3. **Health Check Path:** `/health`
4. **Environment Variable:** `PYTHON_VERSION` = `3.11.4`

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
