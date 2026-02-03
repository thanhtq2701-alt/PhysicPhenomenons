import streamlit as st
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib
import time

# Force Matplotlib to use a non-interactive backend (Fixes blank pages)
matplotlib.use('Agg')

st.set_page_config(page_title="Vibration Simulator", layout="wide")

st.title("🎛️ Interactive Mass-Spring-Damper Simulation")

# --- Sidebar ---
st.sidebar.header("System Parameters")
m = st.sidebar.slider("Mass (m)", 0.1, 10.0, 2.0)
k = st.sidebar.slider("Spring Constant (k)", 1.0, 100.0, 50.0)
c = st.sidebar.slider("Damping (c)", 0.0, 20.0, 1.5)

# --- The Physics with a Spinner ---
with st.spinner('Calculating Dynamics...'):
    # The math is very fast, so the spinner usually blinks. 
    # I'll add a tiny delay so you can actually see it working.
    time.sleep(0.5) 
    
    def system_dynamics(state, t, m, c, k):
        x, v = state
        return [v, (-c*v - k*x) / m]

    t = np.linspace(0, 20, 1000)
    solution = odeint(system_dynamics, [1.0, 0.0], t, args=(m, c, k))
    
    # Create the figure
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(t, solution[:, 0], color='#0077b6')
    ax.set_title("System Response")
    ax.grid(True)

# --- Render the Plot ---
st.pyplot(fig)
st.success("Plot Rendered!")