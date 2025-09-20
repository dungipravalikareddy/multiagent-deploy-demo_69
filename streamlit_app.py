# streamlit_app.py
import streamlit as st
from app.pipeline import run_workflow
from app.utils import check_openai_key

st.set_page_config(page_title="Multi-Agent Demo", layout="centered")
st.title("Multi-Agent Demo — Researcher → Writer")

try:
    check_openai_key()
except Exception as e:
    st.error(str(e))
    st.stop()

topic = st.text_input("Topic to research", value="Impact of AI on Education")
tone = st.selectbox("Tone", options=["neutral", "friendly", "formal"], index=0)
if st.button("Run workflow"):
    with st.spinner("Running researcher..."):
        outputs = run_workflow(topic, tone)
    st.subheader("Researcher notes")
    st.write(outputs["notes"])
    st.subheader("Writer draft")
    st.write(outputs["draft"])

st.markdown("---")
st.info("Deploy: Streamlit Cloud supports mounting secrets; set OPENAI_API_KEY there.")
