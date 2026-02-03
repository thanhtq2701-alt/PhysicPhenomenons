import matplotlib.pyplot as plt
import streamlit as st

def apply_custom_style(fig, ax):
    """
    Applies a consistent dark-theme visual style to Matplotlib plots 
    to match the Streamlit UI.
    """
    # Set dark background colors
    fig.patch.set_facecolor('#0e1117')
    ax.set_facecolor('#1e1e1e')
    
    # Style the grid and spines
    ax.grid(True, linestyle='--', alpha=0.3, color='gray')
    ax.spines['bottom'].set_color('#cccccc')
    ax.spines['top'].set_color('#333333') 
    ax.spines['right'].set_color('#333333')
    ax.spines['left'].set_color('#cccccc')
    
    # Style the labels
    ax.xaxis.label.set_color('#ffffff')
    ax.yaxis.label.set_color('#ffffff')
    ax.tick_params(colors='#ffffff', which='both')
    
    return fig, ax

def format_metric(label, value, unit=""):
    """
    Displays a consistently formatted metric in the toolbox/sidebar.
    """
    st.markdown(f"**{label}**")
    st.code(f"{value:.2f} {unit}")