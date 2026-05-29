import streamlit as st
from login import login_system, logout_button

st.set_page_config(
    page_title="AI MASTER OS",
    page_icon="🚀",
    layout="wide"
)
login_system()
logout_button()

st.markdown("""
# 🚀 AI MASTER OS — LEVEL 37

### Hệ điều hành AI đa trang

✅ Video Studio  
✅ Movie OS  
✅ Brand Empire  
✅ Business Empire  
✅ Automation  
✅ Dashboard
""")