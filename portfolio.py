import streamlit as st
import kumarapp
from PIL import Image

st.set_page_config(page_title="Kumar`s Portfolio",    layout="centered")


def load_profile_image(image):
    try:
        st.image(image,width=300)
    except FileNotFoundError:
        st.error("Profile image not found.")
        return None

st.sidebar.title("WELCOME")
nav_options = ["Home", "About Me", "Skills", "Guessing game", "Contact me"]
nav_choice = st.sidebar.radio("Select a page", nav_options)


if nav_choice == "Home":
    profile_image = load_profile_image("photo2.jpg")
    st.title("Welcome to My Portfolio")
    st.write("My Name is Kumaravel")
    st.write("I`m a First Year B.E Student ")
    st.write("Here you can find information About my skills, projects, and ways to contact me.")
    st.write("---")

elif nav_choice == "About Me":
    profile_image = load_profile_image("photo2.jpg")
    st.header("About Me")
    st.write("""
        I am a Student in an Electronic and Communicaation Engineering.
        \nI love Coding And Solving the Problems
        \nWhen I Got the Errors in My Problem Only I saw "ERROR MAKES CLEVER" Then i go to solve that.     
        \n- *Native:* Tuticorin.
        \n- *Location:* KGiSL Institute Of Technology,Coimbatore. 
        \n- *Education:* UG Degree Ongoing in ECE.
        \n- *Intrest:* Intrest On Learn Something Worthful in my Free Time
        """)
    st.write("---")

elif nav_choice == "Skills":
    
    st.header("Skills")
    st.write("""
    - *Programming Languages:* Python.
    \n- *Web Development:* HTML,CSS.
    \n- *Frameworks:* Flask,Streamlit.
    \n- *Tools:* Git,Git Hub,Autocad.
             
    """)
    st.progress(75)
    st.write("In all of the above i have Learned 80%")
    st.write("---")


elif nav_choice == "Guessing game":
    kumarapp.guessinggame()

elif nav_choice == "Contact me":
    st.header("Contact Me")
    st.write("Feel free to reach out to me at:")
    
    st.write("Email: tkumarvel2006@gmail.com")
    st.write("Phone no: 8015480395")