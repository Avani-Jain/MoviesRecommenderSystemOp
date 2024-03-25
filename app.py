
import pickle
import streamlit as st
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=c3ec758850e7170c74bbd34e8a4ba216&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:11]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


st.header('Movie Recommender System Using Machine Learning')
movies = pickle.load(open('artifacts/movie_list.pkl','rb'))
similarity = pickle.load(open('artifacts/similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    # row1 = st.columns(5)
    # row2 = st.columns(5)
    col11, col21, col31, col41, col51 = st.columns(5)
    col12, col22, col32, col42, col52 = st.columns(5)
    # for i in range(1, 10):
    #     column = "col" + str(i)
    #     with column:
    #         st.text(recommended_movie_names[i-1])
    with col11:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col21:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
    with col31:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col41:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col51:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
    with col12:
        st.text(recommended_movie_names[5])
        st.image(recommended_movie_posters[5])
    with col22:
        st.text(recommended_movie_names[6])
        st.image(recommended_movie_posters[6])
    with col32:
        st.text(recommended_movie_names[7])
        st.image(recommended_movie_posters[7])
    with col42:
        st.text(recommended_movie_names[8])
        st.image(recommended_movie_posters[8])
    with col52:
        st.text(recommended_movie_names[9])
        st.image(recommended_movie_posters[9])