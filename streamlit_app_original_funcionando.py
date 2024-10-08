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
    page_title="Streamly - An Intelligent Streamlit Assistant",
    page_icon="imgs/avatar_streamly.png",
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


# Insert custom CSS for glowing effect
st.markdown(
    """
    <style>
    .cover-glow {
        width: 100%;
        height: auto;
        padding: 3px;
        box-shadow: 
            0 0 5px #330000,
            0 0 10px #660000,
            0 0 15px #990000,
            0 0 20px #CC0000,
            0 0 25px #FF0000,
            0 0 30px #FF3333,
            0 0 35px #FF6666;
        position: relative;
        z-index: -1;
        border-radius: 45px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Load and display sidebar image
img_path = "imgs/sidebar_streamly_avatar.png"
img_base64 =img_to_base64(img_path)
if img_base64:
    st.sidebar.markdown(
        f'<img src="data:image/png;base64,{img_base64}" class="cover-glow">',
        unsafe_allow_html=True,
    )

st.sidebar.markdown("---")

# Sidebar for Mode Selection
mode = st.sidebar.radio("Select Mode:", options=["Latest Updates", "Chat with Streamly"], index=1)

st.sidebar.markdown("---")

# Display basic interactions
show_basic_info = st.sidebar.checkbox("Show Basic Interactions", value=True)
if show_basic_info:
    st.sidebar.markdown("""
    ### Basic Interactions
    - **Ask About Streamlit**: Type your questions about Streamlit's latest updates, features, or issues.
    - **Search for Code**: Use keywords like 'code example', 'syntax', or 'how-to' to get relevant code snippets.
    - **Navigate Updates**: Switch to 'Updates' mode to browse the latest Streamlit updates in detail.
    """)

# Display advanced interactions
show_advanced_info = st.sidebar.checkbox("Show Advanced Interactions", value=False)
if show_advanced_info:
    st.sidebar.markdown("""
    ### Advanced Interactions
    - **Generate an App**: Use keywords like **generate app**, **create app** to get a basic Streamlit app code.
    - **Code Explanation**: Ask for **code explanation**, **walk me through the code** to understand the underlying logic of Streamlit code snippets.
    - **Project Analysis**: Use **analyze my project**, **technical feedback** to get insights and recommendations on your current Streamlit project.
    - **Debug Assistance**: Use **debug this**, **fix this error** to get help with troubleshooting issues in your Streamlit app.
    """)

st.sidebar.markdown("---")

# Load and display image with glowing effect
img_path = "imgs/stsidebarimg.png"
img_base64 = img_to_base64(img_path)
if img_base64:
    st.sidebar.markdown(
        f'<img src="data:image/png;base64,{img_base64}" class="cover-glow">',
         unsafe_allow_html=True,
    )


        
