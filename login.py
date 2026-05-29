import streamlit as st

def login_system():

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if "username" not in st.session_state:
        st.session_state.username = ""

    if not st.session_state.logged_in:

        st.title("🔐 AI MASTER LOGIN SYSTEM")

username = st.text_input("Tên đăng nhập")
password = st.text_input("Mật khẩu", type="password")

        if st.button("🚀 Đăng nhập"):

            if username == "admin" and password == "baudeptrai:

                st.session_state.logged_in = True
                st.session_state.username = username

                st.success("✅ Đăng nhập thành công!")
                st.rerun()

            else:
                st.error("❌ Sai tài khoản hoặc mật khẩu")

        st.stop()

def logout_button():

    st.sidebar.markdown("---")

    st.sidebar.success(f"👤 {st.session_state.username}")

    if st.sidebar.button("🚪 Đăng xuất"):

        st.session_state.logged_in = False
        st.session_state.username = ""

        st.rerun()