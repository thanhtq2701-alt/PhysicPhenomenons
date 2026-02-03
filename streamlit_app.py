import streamlit as st

# Configure the page once at the top level
st.set_page_config(page_title="Physics Lab Suite", layout="wide")

# Define the pages using the standalone files
pg = st.navigation([
    st.Page("modules/vibration.py", title="Vibration Simulation", icon="🏗️"),
    st.Page("modules/optics.py", title="Candle Optics", icon="🕯️"),
    st.Page("modules/about.py", title="About Me", icon="👤"),
])

pg.run()