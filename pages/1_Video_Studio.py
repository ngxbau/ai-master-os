import streamlit as st

st.title("🎬 VIDEO STUDIO")

idea = st.text_area("Ý tưởng video")

if st.button("Tạo Prompt"):

    prompt = f"""
Create cinematic AI video.

IDEA:
{idea}

Style:
Hollywood cinematic

Camera:
dynamic camera movement

Lighting:
dramatic lighting
"""

    st.code(prompt)