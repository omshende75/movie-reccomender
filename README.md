# 🎬 Movie Recommendation System

A hybrid machine learning-based movie recommendation system with a login page, search functionality, and movie posters powered by TMDb. Built using **Python**, **Pandas**, **Scikit-learn**, and **Streamlit**.

![Screenshot](https://user-images.githubusercontent.com/yourusername/sample-screenshot.png) <!-- Optional demo image -->

---

## 🚀 Features

- 🔐 **Login page** with session state
- 🔍 **Fuzzy search** for movie selection
- 🎯 **Hybrid recommender** (collaborative + content-based filtering)
- 🖼️ **Movie posters** via [TMDb API](https://www.themoviedb.org/)
- 🎨 Aesthetic UI with background image & clean layout

---

## 📦 Tech Stack

- Python 3.8+
- Streamlit
- Pandas
- Scikit-learn
- TMDb API

---

## 📁 Project Structure

```
movie-recommender/
├── app.py                # Streamlit UI + login logic
├── recommend.py          # ML logic for movie recommendations
├── data/
│   ├── ratings.csv       # Ratings from MovieLens
│   └── movies.csv        # Movie metadata
├── requirements.txt      # Python dependencies
└── README.md             # Project overview
```

---

## 🔧 Installation & Setup

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/movie-recommender.git
cd movie-recommender
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Download dataset

From [MovieLens (ml-latest-small)](https://grouplens.org/datasets/movielens/ml-latest-small/)  
→ Place `ratings.csv` and `movies.csv` in the `/data` folder.

---

## 🖼️ TMDb API Setup (Optional for Posters)

1. Sign up: https://www.themoviedb.org/
2. Get API key from your profile (Settings → API)
3. Replace the placeholder in `app.py`:

```python
TMDB_API_KEY = "your_tmdb_api_key"
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Then open your browser at:  
http://localhost:8501

---

## 🔐 Login Credentials

| Username | Password  |
|----------|-----------|
| admin    | pass123   |

> You can change these inside `app.py`.

---

## 🎨 Customization

- 🔄 Replace background image in CSS block inside `app.py`
- 💬 Extend login to use real user data
- 📊 Add genre filters, star ratings, or watchlist

---

## 📜 License

Free to use and customize for educational purposes.

---

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io)
- [MovieLens Dataset](https://grouplens.org/datasets/movielens/)
- [TMDb API](https://www.themoviedb.org/)


 
