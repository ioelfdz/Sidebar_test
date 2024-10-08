import streamlit as st
from PIL import Image, ImageEnhance
import time
import json
import requests
import base64
import image


def img_to_base64(image_path):
    """Convert image to base64."""
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except Exception as e:
        logging.error(f"Error converting image to base64: {str(e)}")
        return None

# Streamlit Page Configuration
st.set_page_config(
    page_title="One4All Supervisor Charts",
    page_icon="data/o4a_logo.jpg",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        "Get help": "https://github.com/AdieLaine/Streamly",
        "Report a bug": "https://github.com/AdieLaine/Streamly",
        "About": """
                ## Streamly Streamlit Assistant
                ### Powered using GPT-4o-mini

                **GitHub**: https://github.com/AdieLaine/

                The AI Assistant named, Streamly, aims to provide the latest updates from Streamlit,
                generate code snippets for Streamlit widgets,
                and answer questions about Streamlit's latest features, issues, and more.
                Streamly has been trained on the latest Streamlit updates and documentation.
            """
    }
)

# Streamlit Title
st.title("Streamly Streamlit Assistant")


# Load and display sidebar image
img_path = "data/o4a_logo.png"
img_base64 =img_to_base64(img_path)
if img_base64:
    st.sidebar.markdown(
        f'<img src="data:image/png;base64,{img_base64}" >',
        unsafe_allow_html=True,
    )

st.sidebar.markdown("---")

st.sidebar.markdown("---")


# Load and display image with glowing effect
img_path = "data/schneider-electric-favicon.png"
img_base64 = img_to_base64(img_path)
if img_base64:
    st.sidebar.markdown(
        f'<img src="data:image/png;base64,{img_base64}" >',
         unsafe_allow_html=True,
    )


        
