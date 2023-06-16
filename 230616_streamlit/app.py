import streamlit as st

st.title("나의 파이썬 웹 페이지")
st.header("수업 8일차에 만들었습니다.")
st.subheader("그래도 잘 만들었죠?")
st.write("내가 만든 streamlit 페이지, 너를 위해 구었지")

# streamlit run app.py -> 터미널에 입력하면 지금까지의 현황 파악할 수 있음.

# local URL : 나만 볼 수 있는 네트워크

# 기능이 실행되는 순서대로 화면에서 표현된다.
st.video("http://www.youtube.com/watch?v=SaCheA6Njc4")
st.image("https://cdn.pixabay.com/photo/2013/03/21/15/52/basketball-95607_1280.jpg")
st.image("img/img.png", use_column_width=True)
st.image("img/img.png", width=100)