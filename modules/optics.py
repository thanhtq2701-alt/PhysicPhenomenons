import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Content for the Candle Optics page
st.title("🕯️ Candle Light Convergence")

# --- SIDEBAR: Parameters ---
with st.sidebar:
    st.header("🔍 Lens Parameters")
    n = st.slider("Refractive Index (n)", 1.0, 2.0, 1.5)
    power = st.slider("Lens Convergence", 0.1, 2.0, 0.8)
    
    st.divider()
    st.info("Adjust the sliders to see how the focal point changes based on the lens properties.")

# --- PHYSICS LOGIC ---
# Calculate focal length using the lens maker's approximation from your original code
focal_length = 5 / (power * (n - 0.5))

# --- VISUALIZATION ---
fig, ax = plt.subplots(figsize=(10, 5))

# Ray tracing logic
x_candle = -5
y_rays = np.linspace(-1, 1, 15)

for y in y_rays:
    # Ray from source (candle) to lens
    ax.plot([x_candle, 0], [0, y], color='yellow', alpha=0.3)
    # Ray from lens to focal point
    ax.plot([0, focal_length], [y, 0], color='orange', alpha=0.6)

# Draw lens
ax.add_patch(plt.Circle((0, 0), 1.5, color='lightblue', alpha=0.3))

# Plot styling
ax.axhline(0, color='white', lw=0.5, ls='--') # Optical axis
ax.set_xlim(-6, 8)
ax.set_ylim(-2, 2)
ax.set_facecolor('#1e1e1e')
fig.patch.set_facecolor('#0e1117') # Match Streamlit dark theme

st.pyplot(fig)

# Metrics display
st.success(f"**Calculated Focal Point:** x = {focal_length:.2f}")