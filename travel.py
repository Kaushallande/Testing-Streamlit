import streamlit as st
import pandas as pd
from geopy.distance import geodesic

# Sample data (in a real application, this might be loaded from a database or API)
trekking_data = {
    "name": ["Trek A", "Trek B", "Trek C", "Trek D"],
    "latitude": [28.7041, 27.1739, 31.1048, 26.9124],
    "longitude": [77.1025, 78.0421, 77.1734, 75.7873],
    "cost": [100, 150, 200, 250]
}

# Convert to DataFrame
df = pd.DataFrame(trekking_data)

# Function to calculate distance
def calculate_distance(user_location, trek_location):
    return geodesic(user_location, trek_location).km

# Streamlit app
st.title("Nearest Trekking Points")

# User input for location
user_lat = st.number_input("Enter your latitude", format="%.6f")
user_lon = st.number_input("Enter your longitude", format="%.6f")

if st.button("Find Nearest Treks"):
    if user_lat and user_lon:
        user_location = (user_lat, user_lon)
        df["distance"] = df.apply(lambda row: calculate_distance(user_location, (row["latitude"], row["longitude"])), axis=1)
        nearest_treks = df.sort_values(by="distance").head(5)  # Show top 5 nearest treks

        st.subheader("Nearest Trekking Points")
        for index, row in nearest_treks.iterrows():
            st.write(f"{row['name']} - {row['distance']:.2f} km away, Cost: ${row['cost']}")
    else:
        st.error("Please enter a valid latitude and longitude.")

# To run the app, save this code in a file (e.g., app.py) and run `streamlit run app.py` in the terminal
