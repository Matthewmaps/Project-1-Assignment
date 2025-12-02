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
                        ['🏠 Home', '👔 About', '💼 Projects', '⚒️ Skills', '📝 Resume', '📩 Contact',  ])

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
    st.metric('skills', '4+', '🚀')

  st.write('---')

# Introduction with columns
  col1, col2 = st.columns([2,1])
  with col1:
       st.subheader('Welcome to my digital space!👋')
       st.write('''
                  Hello, my name is Matthew Green. I am a Business Administration student who is currently 
                  studying for an Associate of Science degree in Business Administration. I am currently learning
                  English 150, Business 103, Sociology 101, and Math 136 for this semester. 
              
                  🎯 **Current Focus:** Pursuing My Associate's Degree in Business Administration
              
                  📚 **Currently Learning:** Internet and Emerging Technologies (CIS 211), ENGL 150, SOC 101, BUS 103
              
                  🌱 **Fun Fact:** I Can Repair electronics, such as Computers and Laptops!
              ''')
      
  with col2: 
    # Placeholder for image
    st.image('https://raw.githubusercontent.com/Matthewmaps/Project-1/refs/heads/main/new-york-city-one-world-trade-center-5.JFIF', use_column_width=True)

# About Page
elif page == '👔 About':
  st.title('About Me')

  # Timeline of my Professional Journey
  st.subheader('My Journey 🗺️')

  with st.expander('2024 - Present: Medgar Evers College'):
    st.write('''
                - Major: Business Administration 
                - Relevant Coursework: Internet & Emerging Technologies, Programming, Database Systems, AI
                - Activities: Studying and Learning
            ''')

  with st.expander('2022 - 2024: Pathways 2 Gradutation'):
    st.write('''
                - Graduated with A GED
                - GED Math Score 157
                - Earned a 2024 Recognition Award
            ''')

  st.subheader('Interests & Hobbies 🌳')
  interests = ['Architecture', 'Gaming', 'Exercising', 'Sports Cars', 'Traveling', 'Relaxing']

  # Display the interests in columns
  cols = st.columns(3)
  for i, interest in enumerate(interests):
    with cols[i % 3]:
      st.info(f'🔷 {interest}')
elif page == '💼 Projects':
  st.title('My Projects')
  st.write('Here are some projects I have worked on:')

  # Project 1
  with st.container():
    col1, col2 = st.columns([1, 2])
  
    with col1:
        st.image('https://iprx-cms-content.ams1.vultrobjects.com/Blog_How_To_Crawl_4_capcha_ded9206d5f.png')

    with col2:
        st.subheader('📷 Editor Hiring Advertisment')
        st.write('An Ad campaign aiming to hire new editors')
        st.caption('**Technologies:** Google Ads, Linkdin, Excel')

 # Project 2 
  with st.container():
    col1, col2 = st.columns([1,2])
    with col1:
      st.image('https://www.publicdomainpictures.net/pictures/90000/nahled/calculator-black-clipart.jpg')
    with col2:
      st.subheader('🍽️ Resturant Marketing Campaign')
      st.write('A marketing campaign that plans to attract customers')
      st.caption('**Technologies:** youtube shorts, Tiktok, Instagram')

elif page == '⚒️ Skills':
  st.title('Business Skills')

  # Skills with progress bars
  st.subheader('Marketing Skills')
    
  skills_data = {
    'Business Writing' : 90,
    'Time Management' : 78,
    ' Ad Campaigns' : 75,
    'Media marketing' : 60,
    ' Team Collaberating' : 55
  }
    
  for skill, level in skills_data.items():
    col1, col2 = st.columns([1,3])
    with col1:
      st.write(skill)
    with col2:
      st.progress(level/100)

  st.subheader('Tools & Technologies')

  col1, col2, col3 = st.columns(3)
    
  with col1:
    st.success(' Microsoft Excel')
    st.info('Microsoft Word')
    st.warning('Google Ads')

  with col2:
    st.success('PowerPoint')
    st.info('Google Docs')
    st.warning('Google Slides')
    
  with col3:
    st.success('Canva')
    st.info('Digital Advertising')
    st.warning('Social Media')

elif page == '📝 Resume':
  st.title('Resume')

  # Read PDF from GitHub repository
  with open('my_resume.pdf', 'rb') as pdf_file:
    PDFbyte = pdf_file.read()
  
  st.download_button(
    label ='🔻 Download Full Resume (PDF)',
    data = PDFbyte,
    file_name = 'my_resume.pdf',
    mime ='application/pdf'
  )

elif page == '📩 Contact':
  st.title("Let's Connect!")

  col1, = st.columns(1)

  with col1:
    st.subheader('Send me a message.')

    st.write('''
        📧 **Email:** matthewmaps@gmail.com

        🏢 **LinkedIn:** [linkedin.com/in/yourname](https://linkedin.com)

        👩‍💻 **Github:** [https://github.com/Matthewmaps](https://github.com)

        📷 **Phone Number:** [917-507-4542]

    ''')

    # Fun interactive element
    st.subheader('Current Status')

    status = st.selectbox(
        "I'm currently:",
        [
            '🏫 Learning',
            '📕 Studying',
            '🎮 Gaming',
            '💪 Working out',
            '😴 Sleeping'
        ]
    )


    st.info(f'Status: {status}')

    # Footer
    st.write('---')
    st.markdown(
        f'<center>Made with 💚 using Streamlit | © {datetime.now().year} Matthew Green. </center>',
        unsafe_allow_html = True
    )



    
      
            



