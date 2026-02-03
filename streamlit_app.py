import streamlit as st

st.set_page_config(page_title="Physics & Project Suite", layout="wide")

pg = st.navigation([
    st.Page("modules/vibration.py", title="Vibration Simulation", icon="🏗️"),
    st.Page("modules/optics.py", title="Candle Optics", icon="🕯️"),
    st.Page("modules/calendar_tools.py", title="Project & Calendar", icon="📅"), # Added this
    st.Page("modules/about.py", title="About Me", icon="👤"),
])

pg.run()