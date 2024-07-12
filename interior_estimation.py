import streamlit as st

# Sample cost data (in a real application, this might be loaded from a database)
cost_data = {
    "Living Room": {"Sofa": 500, "Coffee Table": 150, "TV Stand": 200},
    "Bedroom": {"Bed": 700, "Wardrobe": 300, "Dresser": 250},
    "Kitchen": {"Dining Table": 400, "Chairs": 100, "Cabinets": 600},
    "Bathroom": {"Vanity": 300, "Shower": 500, "Toilet": 200}
}

# Function to calculate the total cost
def calculate_cost(rooms):
    total_cost = 0
    for room, items in rooms.items():
        for item, quantity in items.items():
            total_cost += cost_data[room][item] * quantity
    return total_cost

# Streamlit app
st.title("Interior Estimation App")

# User input for different rooms and furniture items
rooms = {}
for room in cost_data.keys():
    st.subheader(room)
    items = {}
    for item in cost_data[room].keys():
        quantity = st.number_input(f"Enter the number of {item}s", min_value=0, max_value=10, value=0, key=f"{room}_{item}")
        if quantity > 0:
            items[item] = quantity
    if items:
        rooms[room] = items

# Calculate and display the total cost when the button is pressed
if st.button("Calculate Total Cost"):
    if rooms:
        total_cost = calculate_cost(rooms)
        st.write(f"The total estimated cost is: ${total_cost}")
    else:
        st.error("Please enter at least one item to estimate the cost.")

# To run the app, save this code in a file (e.g., interior_estimation.py) and run `streamlit run interior_estimation.py` in the terminal
