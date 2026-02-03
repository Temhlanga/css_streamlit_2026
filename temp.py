# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import pandas as pd
import numpy as np

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Temhlanga Malindzisa | Researcher Profile",
    layout="wide"
)

# --------------------------------------------------
# Sidebar Navigation
# --------------------------------------------------
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["Profile", "Publications", "STEM Data Explorer", "Contact"])

# --------------------------------------------------
# Sample STEM Data
# --------------------------------------------------
physics_data = pd.DataFrame({
    "Experiment": ["Alpha Decay", "Beta Decay", "Gamma Ray Analysis", "Quark Study", "Higgs Boson"],
    "Energy (MeV)": [4.2, 1.5, 2.9, 3.4, 7.1],
    "Date": pd.date_range(start="2024-01-01", periods=5),
})

astronomy_data = pd.DataFrame({
    "Celestial Object": ["Mars", "Venus", "Jupiter", "Saturn", "Moon"],
    "Brightness (Magnitude)": [-2.0, -4.6, -1.8, 0.2, -12.7],
    "Observation Date": pd.date_range(start="2024-01-01", periods=5),
})

weather_data = pd.DataFrame({
    "City": ["Cape Town", "London", "New York", "Tokyo", "Sydney"],
    "Temperature (°C)": [25, 10, -3, 15, 30],
    "Humidity (%)": [65, 70, 55, 80, 50],
    "Recorded Date": pd.date_range(start="2024-01-01", periods=5),
})

# --------------------------------------------------
# PROFILE SECTION
# --------------------------------------------------
if menu == "Profile":
    st.title("Researcher Profile")

    col1, col2 = st.columns([1, 2])

    with col1:
        # IMPORTANT: Image must be in the same folder as this script
        st.image(
            "temhlanga.jpg",
            caption="Temhlanga Malindzisa",
            width=220
        )

    with col2:
        st.subheader("Temhlanga Malindzisa")
        st.write("**Field:** Computing & Information Technology")
        st.write("**Institution:** University of Mpumalanga")
        st.write("**Role:** Lecturer & Researcher")
        st.write(
            """
            I am a computing academic with interests in:
            - STEM education
            - Data analysis and visualization
            - Digital learning platforms
            - Technology-enhanced teaching and learning
            """
        )

# --------------------------------------------------
# PUBLICATIONS SECTION
# --------------------------------------------------
elif menu == "Publications":
    st.title("Publications")

    uploaded_file = st.file_uploader(
        "Upload a CSV file containing publications",
        type="csv"
    )

    if uploaded_file:
        publications = pd.read_csv(uploaded_file)
        st.dataframe(publications)

        keyword = st.text_input("Filter publications by keyword")
        if keyword:
            filtered = publications[
                publications.apply(
                    lambda row: keyword.lower() in row.astype(str).str.lower().values,
                    axis=1
                )
            ]
            st.subheader(f"Filtered Results for '{keyword}'")
            st.dataframe(filtered)

        if "Year" in publications.columns:
            st.subheader("Publication Trends by Year")
            st.bar_chart(publications["Year"].value_counts().sort_index())

# --------------------------------------------------
# STEM DATA EXPLORER
# --------------------------------------------------
elif menu == "STEM Data Explorer":
    st.title("STEM Data Explorer")

    data_option = st.selectbox(
        "Choose a dataset",
        ["Physics Experiments", "Astronomy Observations", "Weather Data"]
    )

    if data_option == "Physics Experiments":
        st.dataframe(physics_data)
        energy = st.slider("Energy Range (MeV)", 0.0, 10.0, (0.0, 10.0))
        st.dataframe(
            physics_data[physics_data["Energy (MeV)"].between(*energy)]
        )

    elif data_option == "Astronomy Observations":
        st.dataframe(astronomy_data)
        brightness = st.slider("Brightness Range", -15.0, 5.0, (-15.0, 5.0))
        st.dataframe(
            astronomy_data[astronomy_data["Brightness (Magnitude)"].between(*brightness)]
        )

    elif data_option == "Weather Data":
        st.dataframe(weather_data)

# --------------------------------------------------
# CONTACT SECTION
# --------------------------------------------------
elif menu == "Contact":
    st.title("Contact Information")
    st.write("📧 **Email:** temhlanga.malindzisa@ump.ac.za")
    st.write("🏫 **Institution:** University of Mpumalanga")
