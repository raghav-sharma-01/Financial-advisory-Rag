import streamlit as st
from ui_financial_advisory_tab import render_financial_advisory_tab

st.set_page_config(
    page_title="Financial Advisory RAG",
    page_icon="💰",
    layout="wide"
)

st.title("💰 Financial Advisory RAG")

render_financial_advisory_tab()