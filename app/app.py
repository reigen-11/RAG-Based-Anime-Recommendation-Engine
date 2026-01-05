import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from pipeline.pipeline import AnimeRecommendationPipeline
from dotenv import load_dotenv

# Page configuration
st.set_page_config(
    page_title="Anime Recommendation Engine",
    layout="wide"
)

load_dotenv()

# Initialize session state
if 'history' not in st.session_state:
    st.session_state.history = []
if 'query' not in st.session_state:
    st.session_state.query = ''

@st.cache_resource
def init_pipeline():
    return AnimeRecommendationPipeline()

pipeline = init_pipeline()

# Main title
st.title("Anime Recommendation Engine")
st.markdown("---")

# Example queries section
st.markdown("### Try these examples:")
col1, col2, col3 = st.columns(3)

examples = [
    "Dark psychological thriller anime",
    "Lighthearted school comedy with romance",
    "Epic fantasy adventure with magic"
]

for i, (col, example) in enumerate(zip([col1, col2, col3], examples)):
    with col:
        if st.button(example, key=f"ex_{i}", use_container_width=True):
            st.session_state.query = example
            st.rerun()

query = st.text_input(
    "Enter your anime preferences:",
    value=st.session_state.get('query', ''),
    placeholder="e.g., action anime with strong female lead"
)

if query:
    st.session_state.query = query


if query:
    try:
        with st.spinner("🔍 Searching through 284 anime..."):
            response = pipeline.recommend(query)
            
        # Add to history
        if query not in st.session_state.history:
            st.session_state.history.insert(0, query)
            st.session_state.history = st.session_state.history[:5]  # Keep last 5
        
        # Display success
        st.success("✅ Recommendations ready!")
        
        # Display recommendations
        st.markdown("### 🎬 Recommendations")
        st.markdown(response['answer'])
        
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
        st.info("💡 Please try a different query or check the logs for details.")

# Sidebar with history and info
with st.sidebar:
    st.markdown("## 📊 System Info")
    st.metric("Total Anime", "284")
    st.metric("Model", "Llama 3.1 8B")    
    st.markdown("---")
    
    # Query history
    if st.session_state.history:
        st.markdown("## 📜 Recent Queries")
        for i, q in enumerate(st.session_state.history, 1):
            if st.button(f"{i}. {q[:40]}...", key=f"hist_{i}", use_container_width=True):
                st.session_state.query = q
                st.rerun()
    

    
    