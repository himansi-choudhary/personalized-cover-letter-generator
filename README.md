
# 🚀 Personalized Cover Letter Generator

An AI-powered web application that generates context-aware, role-specific cover letters using Resume and Job Description inputs.
The system focuses on personalization, skill alignment, and analytical feedback to improve job application quality.

---

## 🎯 Project Objective

The objective of this project is to design and implement an intelligent cover letter generation system that:

* Generates personalized cover letters based on Resume + Job Description
* Aligns candidate skills with job requirements
* Provides similarity and matching analysis
* Offers improvement suggestions for better application quality

---

## ✨ Key Features

* Context-aware cover letter generation (Resume + JD)
* Tone customization (Fresher, Mid-level, Experienced)
* Skill match percentage analysis
* Missing skills identification
* Similarity scoring (Cosine Similarity & Jaccard Similarity)
* Resume and Job Description file upload (PDF, DOCX, TXT)
* Web-based interface with REST API support
* CLI-based generation option

---

## 🛠 Tech Stack

**Frontend**

* HTML
* CSS
* JavaScript

**Backend**

* Python
* Flask

**NLP & ML Techniques**

* TF-IDF Vectorization
* Cosine Similarity
* Jaccard Similarity
* Skill Extraction Logic

**Libraries Used**

* NLTK
* Scikit-learn
* Pandas
* PyPDF2
* python-docx

---

## 📁 Project Structure

```
personalized-cover-letter-generator/
├── backend/
│   ├── api.py
│   ├── generator.py
│   ├── matcher.py
│   ├── similarity.py
│   ├── vectorizer.py
│   ├── document_reader.py
│   └── __init__.py
├── templates/
│   ├── index.html
│   └── home.html
├── advanced_generator.py
├── requirements.txt
├── start.bat
└── README.md
```

---

## 🌐 How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone <repository-link>
cd personalized-cover-letter-generator
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Download Required NLTK Data (First Time Only)

```python
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')
```

### 4️⃣ Run the Application

**Option 1: Start Web Server (Recommended)**

```bash
python backend/api.py
```

Access at:

```
http://localhost:5000
```

**Option 2: Run CLI Version**

```bash
python advanced_generator.py
```

---

## 🔍 Core Functionalities

### 📄 Cover Letter Generation

* Takes Resume and Job Description as input
* Extracts relevant skills and experience
* Generates a personalized and role-specific cover letter

### 📊 Matching & Analysis

* Skill alignment scoring
* Cosine similarity between resume and job description
* Jaccard similarity analysis
* Missing skills identification
* Improvement suggestions

### 📤 File Support

* PDF (.pdf)
* Word (.docx)
* Text (.txt)

---

## 👥 Team Contributions

**Darshini – Backend Development**

* Backend logic implementation
* API structure and request handling

**Indhu – Backend Development**

* Resume and Job Description processing
* Matching and analysis logic

**Nil – Backend Development**

* Cover letter generation engine
* NLP and similarity algorithms

**Himansi – Frontend Development**

* UI design and layout
* Form creation (Resume, JD, Tone selection)
* Result display interface

**Pritam – JavaScript & Integration**

* Frontend-backend integration
* API call handling and dynamic updates

**Pratham – Testing & Quality Assurance**

* Functional testing
* Feature validation and bug reporting

---

## 📌 Conclusion

This project demonstrates the practical implementation of NLP-based text generation and similarity analysis in a real-world job application scenario.
The system enhances personalization, improves skill alignment, and provides analytical insights to support better cover letter creation.

---
