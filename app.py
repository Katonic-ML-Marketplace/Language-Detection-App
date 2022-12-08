from googletrans  import Translator
import streamlit as st
from PIL import Image

im = Image.open('image/favicon.ico')

st.set_page_config(page_title='Language Detection',
                   page_icon=im,
                   layout='centered',
                   initial_sidebar_state='auto')

st.image('image/logo.png')
st.title("Language Detection ")

def user_input_features():
    text = st.text_input("Enter any text in any language: ")
    return text

p = user_input_features()

if st.button('Prediction'):
    translator = Translator()
    lang = translator.translate(p,dest='en').src
    st.subheader("Language Detected")
    st.success(lang)
    st.subheader("Translated Text")
    translate_text = translator.translate(p,dest='en').text
    st.success(translate_text)
else:
    st.info("Please enter any text ")