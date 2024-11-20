import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Title
st.title("🌳 Genealogy Explorer")
st.title("🌍 Ancestor Geographic Map")
st.write("Visualize your ancestors' birthplaces and migration patterns on an interactive map!")

# Sidebar for Data Upload
st.sidebar.header("Upload Ancestor Data")
uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    try:
        # Load data
        data = pd.read_csv(uploaded_file)
        st.success("Ancestor data successfully loaded!")
        st.write("### 📋 Uploaded Data:")
        st.dataframe(data)

        # Create the map
        st.write("### 🌟 Ancestor Map Visualization")
        if all(col in data.columns for col in ["Name", "Latitude", "Longitude", "EventDate"]):
            # Initialize map centered around the average location
            center_lat = data["Latitude"].mean()
            center_lon = data["Longitude"].mean()
            # control_scale = data["Longitude"].mean()
            m = folium.Map(location=[center_lat, center_lon], zoom_start=2)

            # Add markers for each ancestor
            for _, row in data.iterrows():
                popup_info = f"""
                <b>Name:</b> {row['Name']}<br>
                <b>Location:</b> {row['Birthplace']}<br>
                <b>Date:</b> {row['EventDate']}
                """
                folium.Marker(
                    [row["Latitude"], row["Longitude"]],
                    popup=popup_info,
                    icon=folium.Icon(color="blue", icon="info-sign")
                ).add_to(m)

            # Render map in Streamlit
            st_map = st_folium(m, width=700, height=500)
        else:
            st.error("The CSV file must have 'Name', 'Latitude', 'Longitude', and 'EventDate' columns.")

        # Search Functionality
        st.write("### 🔎 Search for a Relative and their location 🏡")
        if not data.empty:  # Ensure 'data' is loaded before searching
            search_name = st.text_input("Enter a name to search:")
            if search_name:
                results = data[data["Name"].str.contains(search_name, case=False, na=False)]
                if not results.empty:
                    st.write("### 🎯 Search Results:")
                    st.dataframe(results)
                else:
                    st.warning("No relatives found with that name.")
        else:
            st.info("Search functionality will be available after uploading a file.")

    except Exception as e:
        st.error(f"Error processing the file: {e}")
else:
    st.write("📂 Upload a CSV file to display the ancestor map.")










