import streamlit as st
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Content for the Vibration page
st.title("🏗️ Mass-Spring-Damper System")

with st.sidebar:
    st.header("⚙️ Parameters")
    m = st.slider("Mass (m)", 0.1, 20.0, 5.0)
    k = st.slider("Stiffness (k)", 1.0, 200.0, 100.0)
    c = st.slider("Damping (c)", 0.0, 50.0, 2.0)
    
    st.divider()
    st.subheader("Initial States")
    x0 = st.number_input("Position (x0)", value=1.0)
    v0 = st.number_input("Velocity (v0)", value=0.0)

# Physics Calculation
t = np.linspace(0, 20, 1000)
sol = odeint(lambda state, t: [state[1], (-c*state[1] - k*state[0])/m], [x0, v0], t)

# Visualization
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(t, sol[:, 0], color='#2a9d8f', lw=2)
ax.set_ylabel("Amplitude (m)")
ax.set_xlabel("Time (s)")
st.pyplot(fig)