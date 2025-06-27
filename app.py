import streamlit as st
st.set_page_config(page_title="Movie Recommender 🎬", layout="centered")

import pandas as pd
import requests
from recommend import load_data, preprocess_data, recommend_movies
from difflib import get_close_matches

TMDB_API_KEY = "PLACEHOLDER"  # Replace with your TMDb API key

# ---------- Login ----------
def check_login(username, password):
    return username == "admin" and password == "pass123"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("🔐 Login to Movie Recommender")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if check_login(username, password):
            st.session_state.logged_in = True
            st.success("✅ Login successful!")
        else:
            st.error("❌ Invalid username or password.")
    st.stop()

# ---------- Main App ----------


st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🎬 Movie Recommendation System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Discover movies you'll love — powered by ML and TMDb.</p>", unsafe_allow_html=True)
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1524985069026-dd778a71c7b4");
        background-attachment: fixed;
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
    }
    .block-container {
        backdrop-filter: blur(8px);
        background-color:#fffff(255, 255, 255, 0.75);
        border-radius: 10px;
        padding: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.sidebar.title("Navigation")
st.sidebar.markdown("### Welcome to the Movie Recommender!")
st.sidebar.markdown("Use the search bar to find movies and get recommendations based on your preferences.")
st.sidebar.markdown("---")


if st.button("🚪 Logout"):
    st.session_state.logged_in = False
    st.success("You have been logged out. Please refresh the page or rerun the app.")
    st.stop()


ratings, movies = load_data()
user_movie_matrix, movie_sim, genre_sim, genre_index = preprocess_data(ratings, movies)
movie_titles = movies['title'].values
movie_ids = movies.set_index('title')['movieId'].to_dict()

st.subheader("🔍 Search for a movie")
search_input = st.text_input("Type part of a movie title")
selected_movie = None

if search_input:
    match = get_close_matches(search_input, movie_titles, n=1, cutoff=0.5)
    if match:
        selected_movie = match[0]
        st.info(f"Did you mean: **{selected_movie}**?")
    else:
        st.warning("No match found. Try another title.")

def get_movie_card(title, api_key):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={title}"
    response = requests.get(url)
    if response.status_code == 200:
        results = response.json().get("results", [])
        if results:
            movie = results[0]
            poster = movie.get("poster_path")
            overview = movie.get("overview", "No description available.")
            year = movie.get("release_date", "")[:4]
            poster_url = f"https://image.tmdb.org/t/p/w200{poster}" if poster else ""
            return f'''
                <div style="display: flex; background-color: #f9f9f9; margin-bottom: 20px; border-radius: 10px; overflow: hidden;">
                    <img src="{poster_url}" style="width: 100px; height: auto;">
                    <div style="padding: 10px;">
                        <h4>{title} ({year})</h4>
                        <p style="font-size: 13px;">{overview[:200]}...</p>
                    </div>
                </div>
            '''
    return f"<div style='margin-bottom: 15px;'><b>{title}</b></div>"

if selected_movie:
    if st.button("🎯 Recommend"):
        with st.spinner("Finding similar movies..."):
            movie_id = movie_ids.get(selected_movie)
            if movie_id not in user_movie_matrix.columns:
                st.warning("⚠️ This movie has no rating data.")
            else:
                movie_sim_df = pd.DataFrame(movie_sim, index=user_movie_matrix.columns, columns=user_movie_matrix.columns)
                genre_sim_df = pd.DataFrame(genre_sim, index=genre_index, columns=genre_index)
                recommendations = recommend_movies(movie_id, movie_sim_df, genre_sim_df, movies)

                if recommendations.empty:
                    st.warning("No recommendations found.")
                else:
                    st.success("✅ Top 5 Movies You Might Like:")
                    for _, row in recommendations.iterrows():
                        st.markdown(get_movie_card(row['title'], TMDB_API_KEY), unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 13px;'>🚀 Built with ❤️ using Streamlit and TMDb</p>", unsafe_allow_html=True)
