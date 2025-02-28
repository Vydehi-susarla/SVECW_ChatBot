import streamlit as st
import pandas as pd
import google.generativeai as genai
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

st.title("Chatbot - SVECW")

if "messages" not in st.session_state:
    st.session_state.messages = []
csv_url="svecw_details.csv
