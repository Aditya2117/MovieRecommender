import streamlit as st
import pickle
import requests
# https://api.themoviedb.org/3/movie/19995?api_key=4f3832c58181b3f3a0536ddbd432ed9e&language=en-US

def get_poster_image(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=4f3832c58181b3f3a0536ddbd432ed9e&language=en-US".format(movie_id))
    json_data = response.json()
    return "https://image.tmdb.org/t/p/w500/"+json_data['poster_path']
def Recommend(movie):
    recommended_poster_path = []
    movie_index = movies1[movies1['title'] == movie].index[0]
    movie_rec = []
    temp_sim = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])
    for i in range(1, 6):
        movie_rec.append(movies1['title'][temp_sim[i][0]])
        movie_id_tmdb = movies1['movie_id'][temp_sim[i][0]]
        recommended_poster_path.append(get_poster_image(movie_id_tmdb))
    return movie_rec,recommended_poster_path


similarity = pickle.load(open('sim.pkl', 'rb'))

movies1 = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies1['title'].values
st.header('Aditya Movie Recommender', divider='rainbow')
st.title(":black-background[Made by Aditya Narayan Sharma]")

sel_mov_name = st.selectbox(
    "Please Choose a movie to get recommendations",
    movies_list)
if st.button("Recommend", type="primary"):
    recommendations,recommended_image = Recommend(sel_mov_name)
    col1, col2, col3,col4,col5 = st.columns(5)

    with col1:
        st.text(recommendations[0])
        st.image(recommended_image[0])

    with col2:
        st.text(recommendations[1])
        st.image(recommended_image[1])

    with col3:
        st.text(recommendations[2])
        st.image(recommended_image[2])
    with col4:
        st.text(recommendations[3])
        st.image(recommended_image[3])
    with col5:
        st.text(recommendations[4])
        st.image(recommended_image[4])