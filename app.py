# app.py

import streamlit as st

# Set page title and icon
st.set_page_config(page_title="🚀 My Python Website", page_icon="🌐")

# Add a colorful title
st.markdown(
    """
    <style>
    .title {
        font-size: 40px;
        font-weight: bold;
        color: white;
        background-color: #FF5733;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
    }
    </style>
    <div class="title">🚀 My Python Website 🌐</div>
    """,
    unsafe_allow_html=True
)

# Add a colorful header
st.markdown(
    """
    <style>
    .header {
        font-size: 30px;
        font-weight: bold;
        color: #33FF57;
        text-align: center;
    }
    </style>
    <div class="header">✨ Welcome to My Website! ✨</div>
    """,
    unsafe_allow_html=True
)

# Add a navigation menu
st.markdown(
    """
    <style>
    .nav {
        font-size: 20px;
        font-weight: bold;
        color: #33A8FF;
        text-align: center;
    }
    </style>
    <div class="nav">
        <a href="#home">🏠 Home</a> | 
        <a href="#about">📝 About</a> | 
        <a href="#contact">📧 Contact</a>
    </div>
    """,
    unsafe_allow_html=True
)

# Home Section
st.markdown("<a name='home'></a>", unsafe_allow_html=True)
st.markdown(
    """
    <style>
    .section {
        font-size: 25px;
        font-weight: bold;
        color: #FFA500;
        text-align: center;
    }
    </style>
    <div class="section">🏠 Home</div>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    .text1 {
        font-size: 18px;
        color: #fa2e23 !important;
        text-align: center;
    }
    </style>
    <div class="text1">Welcome to my Python-powered website! This site is built using Streamlit, a powerful tool for creating web apps in Python.</div>
    """,
    unsafe_allow_html=True
)

# About Section
st.markdown("<a name='about'></a>", unsafe_allow_html=True)
st.markdown(
    """
    <style>
    .section {
        font-size: 25px;
        font-weight: bold;
        color: #fa2e23;
        text-align: center;
    }
    </style>
    <div class="section">📝 About</div>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    .text2 {
        font-size: 18px;
        color: #04e01a !important;
        text-align: center;
    }
    </style>
    <div class="text2">This website is a demonstration of how easy it is to build a web app using Streamlit. It includes a homepage, an about section, and a contact form.</div>
    """,
    unsafe_allow_html=True
)

# Contact Section
st.markdown("<a name='contact'></a>", unsafe_allow_html=True)
st.markdown(
    """
    <style>
    .section {
        font-size: 25px;
        font-weight: bold;
        color: #FFA500;
        text-align: center;
    }
    </style>
    <div class="section">📧 Contact</div>
    """,
    unsafe_allow_html=True
)


# Contact form
with st.form("contact_form"):
    st.markdown('<p style="color: blue; font-weight: bold; font-size: 20px;">👤 Name</p>', unsafe_allow_html=True)
    name = st.text_input("", key="name")

    st.markdown('<p style="color: blue; font-weight: bold; font-size: 20px;">📧 Email</p>', unsafe_allow_html=True)
    email = st.text_input("", key="email")

    st.markdown('<p style="color: blue; font-weight: bold; font-size: 20px;">💬 Message</p>', unsafe_allow_html=True)
    message = st.text_area("", key="message")
    submit_button = st.form_submit_button("🚀 Submit")

    if submit_button:
        st.markdown(
            f"""
            <style>
            .success {{
                font-size: 20px;
                font-weight: bold;
                color: #33FF57;
                text-align: center;
            }}
            </style>
            <div class="success">🎉 Thank you, {name}! Your message has been sent.</div>
            """,
            unsafe_allow_html=True
        )

# Add a colorful footer
st.markdown(
    """
    <style>
    .footer {
        font-size: 20px;
        color: #33C1FF;
        text-align: center;
        margin-top: 50px;
    }
    </style>
    <div class="footer">🚀 Thanks for visiting my website! 🚀</div>
    """,
    unsafe_allow_html=True
)

st.markdown('<h6 style="color: red; text-align: center; margin-top: 20px;">📓✒️ Author: Azmat Ali 📓✒️</h6>', unsafe_allow_html=True)
