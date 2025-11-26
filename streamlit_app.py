import streamlit as st
import pandas as pd 
from datetime import datetime

# Page Config
st.set_page_config(
    page_title ='Matthew Green | Portfolio',
    page_icon='🟢',
    layout="wide"
)

# Custom CSS (optional - for styling)
st.markdown('''
    <style>
        .main-header{font-size: 42px; font-weight: bold; text-align:center;}
        .sub-header {font_size: 24px; text-align:center; color: #666;}
      </style>
      ''', unsafe_allow_html = True)

# Sidebar
st.sidebar.title('📍Navigation')
page = st.sidebar.radio('Go to',
                        ['🏠 Home', '👔 About', '💼 projects', '⚒️ Skills', '📝 Resume', '📩 Contact' ])

# Home Page
if page == '🏠 Home':
  st.markdown('<p class="main-header">Matthew Green</p>', unsafe_allow_html=True)
  st.markdown('<p class="sub-header">Undergraduate Student | Medagar Evers College</p>', unsafe_allow_html=True)

  # Three columns for stats 
  col1, col2, col3 = st.columns(3)

  with col1:
    st.metric ('GPA', '3.5', '📚')
  with col2: 
    st.metric('Projects', '5', '💻')
  with col3:
    st.metric('skills', '10+', '🚀')


  st.write('---')

# Introduction with columns
  col1, col2 = st.columns([2,1])
  with col1:
       st.subheader('Welcome to my digital space!👋')
       st.write('''
                  I am a Computer Information Systems student passionate about web development and emerging technologies. Currently learning
                  HTML, CSS, JavaScript, and Python to build innovative solutions.
              
                  🎯 **Current Focus:** Pursing My Business Administration Degree
              
                  📚 **Currently Learning:** Internet and Emerging Technologies (CIS 211)
              
                  🌱 **Fun Fact:** I Can Repair electronics, such as Computers and Laptops
              ''')
  with col2: 
    # Placeholder for image
    st.image('https://raw.githubusercontent.com/avinashjairam/cis211_project1/refs/heads/main/grumpy_cat.jfif', use_column_width=True)


