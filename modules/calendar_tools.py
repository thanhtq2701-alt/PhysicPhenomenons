import streamlit as st
import pandas as pd
import calendar
from datetime import datetime

def get_days_in_month(year, month):
    """Returns the total number of days in a specific month/year."""
    return calendar.monthrange(year, month)[1]

def run_calendar():
    st.title("📅 Project Tracking & Date Tools")
    
    # --- TASK 1: Days in Month Calculator ---
    st.subheader("Month Day Counter")
    c1, c2 = st.columns(2)
    with c1:
        year = st.number_input("Year", min_value=1900, max_value=2100, value=datetime.now().year)
    with c2:
        month = st.selectbox("Month", range(1, 13), format_func=lambda x: calendar.month_name[x])
    
    total_days = get_days_in_month(year, month)
    st.info(f"The total number of days in **{calendar.month_name[month]} {year}** is **{total_days}**.")

    st.divider()

    # --- TASK 2: Google Sheet Data ---
    st.subheader("Project Data (from Source)")
    
    # Public CSV Export Link for the Google Sheet provided
    sheet_url = "https://docs.google.com/spreadsheets/d/16Rj0C47wd8UXyUNInWbq8ZlirW9zZANHf6JPyvcsolw/export?format=csv"
    
    try:
        df = pd.read_csv(sheet_url)
        
        # Display the Raw Data
        st.dataframe(df, use_container_with_width=True)
        
        # Simple Analysis based on the sheet info (Tasks/Personnel)
        if not df.empty:
            st.write("### Quick Summary")
            col_a, col_b = st.columns(2)
            col_a.metric("Total Tasks", len(df))
            
            # Identify columns based on sheet (Assumed columns: Task, Duration, Owner)
            # You can add more complex analysis here
    except Exception as e:
        st.error(f"Could not connect to Google Sheet. Error: {e}")