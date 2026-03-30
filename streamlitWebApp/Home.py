# Home.py
from streamlit_option_menu import option_menu
import streamlit as st
import requests
import time
import pickle
import numpy as np

# ────────────────────────────────────────────────
#   CONFIG
# ────────────────────────────────────────────────
TMDB_API_KEY = "c3c775a1fab54e24e2fcbb4cec15b9f6"
IMG_BASE     = "https://image.tmdb.org/t/p/w500"
IMG_SMALL    = "https://image.tmdb.org/t/p/w185"

# ────────────────────────────────────────────────
#   TMDB SEARCH - multiple results, resilient connection
# ────────────────────────────────────────────────
def search_movies_tmdb(query: str, max_results: int = 12):
    if not query or not query.strip():
        return []

    query = query.strip()

    session = requests.Session()
    adapter = requests.adapters.HTTPAdapter(pool_connections=1, pool_maxsize=1, max_retries=3)
    session.mount('https://', adapter)

    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
        "Accept": "application/json",
        "Connection": "close"
    })

    url = "https://api.themoviedb.org/3/search/movie"

    params = {
        "api_key": TMDB_API_KEY,
        "query": query,
        "include_adult": False,
        "language": "en-US",
    }

    for attempt in range(5):
        try:
            response = session.get(url, params=params, timeout=15)
            response.raise_for_status()
            data = response.json()

            movies = []
            for m in data.get("results", [])[:max_results]:
                poster = IMG_BASE + m["poster_path"] if m.get("poster_path") else None
                small_poster = IMG_SMALL + m["poster_path"] if m.get("poster_path") else None

                movies.append({
                    "id": m.get("id"),
                    "title": m.get("title", "—"),
                    "year": (m.get("release_date") or "")[:4] or "—",
                    "rating": m.get("vote_average", 0),
                    "overview": m.get("overview", "No overview available."),
                    "poster": poster,
                    "small_poster": small_poster
                })
            return movies

        except requests.exceptions.RequestException as e:
            if attempt == 4:
                st.error(f"TMDB connection failed after retries.\nError: {str(e)}\nTry mobile hotspot or pause antivirus.")
                return []
            time.sleep(2 ** attempt + 0.5)

    return []


# ────────────────────────────────────────────────
#   Recommender data loader
# ────────────────────────────────────────────────
@st.cache_resource
def load_recommender_data():
    similarities = []
    for i in range(15):
        with open(f"similarity_chunk_{i+1}.pkl", "rb") as f:
            similarities.append(pickle.load(f))
    similarity = np.concatenate(similarities, axis=0)
    movies_list = pickle.load(open("movies.pkl", "rb"))
    return similarity, movies_list


def recommend_from_dataset(selected_movie):
    similarity, movies_list = load_recommender_data()
    try:
        movie_index = movies_list[movies_list['title'] == selected_movie].index[0]
    except:
        return [], []

    distances = similarity[movie_index]
    sorted_movies = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    names = []
    posters = []

    for idx, _ in sorted_movies:
        name = movies_list.iloc[idx].title
        tmdb_results = search_movies_tmdb(name, max_results=1)
        poster = tmdb_results[0]["poster"] if tmdb_results else None
        names.append(name)
        posters.append(poster)

    return posters, names


# ────────────────────────────────────────────────
#   MAIN UI - no use_column_width anywhere
# ────────────────────────────────────────────────
def main():
    st.title("🎬 Movie Recommender & Explorer")

    # Global search section
    st.subheader("🌍 Search any movie (like TMDB / Netflix)")
    query = st.text_input(
        "",
        placeholder="jailer, kgf, pushpa, war, avengers, bahubali...",
        label_visibility="collapsed"
    )

    if query.strip():
        with st.spinner("Searching..."):
            results = search_movies_tmdb(query)

        if results:
            cols = st.columns(4)
            for i, movie in enumerate(results):
                with cols[i % 4]:
                    if movie["small_poster"]:
                        st.image(movie["small_poster"], width=185)
                    else:
                        st.image("https://placehold.co/185x278?text=No+Poster", width=185)

                    st.markdown(f"**{movie['title']}**")
                    st.caption(f"{movie['year']} • ★ {movie['rating']:.1f}")

                    with st.expander("Overview"):
                        st.write(movie["overview"][:160] + "..." if len(movie["overview"]) > 160 else movie["overview"])
        else:
            st.info("No results or connection issue – check error above if any")

    st.divider()

    # ML Recommender section
    st.subheader("🤖 Recommendations of your choice")

    try:
        _, movies_list = load_recommender_data()
        selected = st.selectbox(
            "Choose a movie from dataset",
            [""] + sorted(movies_list["title"].values.tolist()),
            index=0
        )

        if selected and st.button("Get Recommendations"):
            with st.spinner("Loading recommendations..."):
                posters, names = recommend_from_dataset(selected)

            if names:
                rec_cols = st.columns(5)
                for i in range(min(5, len(names))):
                    with rec_cols[i]:
                        if posters[i]:
                            st.image(posters[i], width=220)
                        else:
                            st.image("https://placehold.co/220x330?text=No+Poster", width=220)
                        st.caption(names[i])
            else:
                st.warning("No recommendations found")
    except Exception as e:
        st.error(f"Model loading failed: {str(e)}")


if __name__ == "__main__":
    main()
