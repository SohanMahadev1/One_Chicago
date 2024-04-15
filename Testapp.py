import streamlit as st
import pandas as pd
import geocoder
import geopy.distance

def get_current_location():
    # Get location using IP
    g = geocoder.ip('me')
    return g.latlng

def fetch_closest_washroom(lat, lon, df):
    closest_washroom = None
    min_distance = float('inf')  # Initialize with a very large number
    for _, row in df.iterrows():
        dist = geopy.distance.distance((lat, lon), (row['Latitude'], row['Longitude'])).km
        if dist < min_distance:
            min_distance = dist
            closest_washroom = row
    return closest_washroom

# Correcting column names and loading washrooms data
df_washrooms = pd.read_csv('bath.csv')
df_washrooms.columns = df_washrooms.columns.str.strip()  # Removing any trailing spaces in column names

st.title('Welcome to the Hackathon Project')
st.header('Public Washroom Finder')

lat = st.number_input("Enter Latitude:", format="%.6f")
lon = st.number_input("Enter Longitude:", format="%.6f")

if st.button("Search Nearby Washrooms"):
    if lat and lon:
        closest_washroom = fetch_closest_washroom(lat, lon, df_washrooms)
        if closest_washroom is not None:
            st.write(f"Closest Washroom: {closest_washroom['Title']}")
            st.write(f"Notes: {closest_washroom['Note']}")
            st.markdown(f"[View on Google Maps]({closest_washroom['URL']})")
        else:
            st.error("No washrooms found near this location.")
    else:
        st.error("Please enter valid latitude and longitude.")

if st.button("Use Current Location"):
    latlng = get_current_location()
    if latlng:
        closest_washroom = fetch_closest_washroom(latlng[0], latlng[1], df_washrooms)
        if closest_washroom is not None:
            st.write(f"Closest Washroom: {closest_washroom['Title']}")
            st.write(f"Notes: {closest_washroom['Note']}")
            st.markdown(f"[View on Google Maps]({closest_washroom['URL']})")
        else:
            st.error("No washrooms found near your current location.")
    else:
        st.error("Could not determine your current location.")
