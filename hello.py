import pandas as pd
import streamlit as st
st.title("Streamlit Practice")
st.write("hello")
st.write("world")
st.write("Hi")
button1= st.button("Click Here")
if button1:
    st.write("This is some text")
chkbx1 = st.checkbox("Do you like strealite")
button2=st.button("Submit")
if button2:
    if chkbx1:
        st.write("Thanks")
    else:
        st.write("We are improving")

x=st.text_input("Favourite Movie?")
st.write(f"Your Favourite Movie is: {x}")
st.write("# Tile Header")
st.write("## Header 1")
st.write("### Header 2")
st.write("#### Header 3")


df=pd.read_csv("marvel - Copy.csv")
st.write(df)

st.write(df.columns)

columns=st.multiselect("Select column tofilter on", df.columns)
filtered_df = df.copy()

for col in columns:
    vals = st.multiselect(f"Select values for {col}", df[col].unique())
    if vals:
        filtered_df = filtered_df[filtered_df[col].isin(vals)]

st.dataframe(filtered_df)

button1=st.button("Print")
if button1:

    st.write(filtered_df)
