import streamlit as st
import json
import os

st.set_page_config(page_title="IndiArchive - Indian Culture & History", layout="wide")

st.sidebar.title("Explore IndiArchive")
page = st.sidebar.radio("Go to", ["Home", "Art", "History", "Culture"])

def load_data(category):
    path = f"data/{category.lower()}.json"
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

if page == "Home":
    st.title("🇮🇳 IndiArchive")
    st.markdown("""
    Welcome to **IndiArchive**, a digital archive that celebrates the diversity, richness,
    and history of **Indian culture**. Explore centuries-old traditions, legendary heroes,
    local arts, festivals, and untold village stories all in one place.
    """)
    if os.path.exists("images/india-banner.jpg"):
        st.image("images/india-banner.jpg", use_column_width=True)
    else:
        st.warning("Banner image not found. Please add 'india-banner.jpg' in the 'images' folder.")

elif page in ["Art", "History", "Culture"]:
    st.title(f"📂 {page} of India")
    stories = load_data(page)

    if stories:
        for story in stories:
            with st.container():
                st.subheader(story['title'])
                image_path = f"images/{story.get('image', '')}"
                if story.get('image') and os.path.exists(image_path):
                    st.image(image_path, width=500)
                elif story.get('image'):
                    st.warning(f"Image '{story['image']}' not found in images folder.")
                st.markdown(f"**Author**: {story['author']}  |  **Date**: {story['date']}")
                st.markdown(story['content'])
                st.markdown("---")
    else:
        st.info(f"No {page} stories added yet. Coming soon!")