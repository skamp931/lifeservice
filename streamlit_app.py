import streamlit as st
import time

st.write("テストページ")

# Using object notation
with st.sidebar:
    add_selectbox = st.selectbox(
    "マネー情報",
    ("幼稚園", "小学生", "高校生", "大学生")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )

if add_selectbox =="幼稚園":
    st.write("幼稚園の時にかかる費用")
    st.write("園児")

if add_selectbox =="小学生":
    st.write("小学生の時にかかる費用")
    st.write("小学")

if add_selectbox =="高校生":
    st.write("高校生の時にかかる費用")
    st.write("高校")

with st.sidebar:
#    with st.echo():
#        st.write("This code will be printed to the sidebar.")

#    with st.spinner("Loading..."):
#        time.sleep(5)
    st.success("Done!")
    
