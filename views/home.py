import streamlit as st
import pickle
import pandas as pd


def fetch_poster(song_name,new_df):
    full_path = new_df.query(f"song == '{song_name}'")["thumbnail"]
    return full_path

def recommand(song, musics, similarity,new_df):
    music_index = musics[musics['song'] == song].index[0]
    distances = similarity[music_index]
    musics_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[0:13]

    recommanded_music = []
    recommanded_music_poster = []

    for i in musics_list:
        song_name = musics.iloc[i[0]].song
        # fetch poster from new-df csv
        recommanded_music_poster.append(fetch_poster(song_name,new_df))
        # fetch movie title
        recommanded_music.append(musics.iloc[i[0]].song)

    return recommanded_music, recommanded_music_poster

def setTextPoster(names,posters,new_df):
    st.text(names)
    img_id_0 = posters.index[0]
    img_0 = new_df.thumbnail[img_id_0]
    st.image(img_0)


def load_view(authenticator=None,name=None):
    music_dict = pickle.load(open('G:\\MyCodeprojects\\Minor Project\\streamlit music recommendation\\views\\models\\music_dict.pkl', 'rb'))
    similarity = pickle.load(open('G:\\MyCodeprojects\\Minor Project\\streamlit music recommendation\\views\\models\\similarity.pkl', 'rb'))
    new_df = pd.read_csv("G:\\MyCodeprojects\\Minor Project\\streamlit music recommendation\\views\\models\\data.csv")

    musics = pd.DataFrame(music_dict)

    st.title("Music recommendation system")

    music_list = musics['song'].values
    music_name = st.selectbox(
        "Type or select a music from the dropdown",
        music_list
    )

    if st.button("Recommand"):
        names, posters = recommand(music_name,musics,similarity,new_df)
        col1, col2, col3, col4, col5, col6 = st.columns(6)
        col7, col8, col9, col10, col11, col12 = st.columns(6)

        with col1:
            setTextPoster(names[0], posters[0],new_df)
        with col2:
            setTextPoster(names[1], posters[1],new_df)
        with col3:
            setTextPoster(names[2], posters[2],new_df)
        with col4:
            setTextPoster(names[3], posters[3],new_df)
        with col5:
            setTextPoster(names[4], posters[4],new_df)
        with col6:
            setTextPoster(names[5], posters[5],new_df)

        with col7:
            setTextPoster(names[6], posters[6],new_df)
        with col8:
            setTextPoster(names[7], posters[7],new_df)
        with col9:
            setTextPoster(names[8], posters[8],new_df)
        with col10:
            setTextPoster(names[9], posters[9],new_df)
        with col11:
            setTextPoster(names[10], posters[10],new_df)
        with col12:
            setTextPoster(names[11], posters[11],new_df)


