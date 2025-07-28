import streamlit as st

st.title("HR Employee Portal")

# --- Get User by ID ---
st.subheader("Get User by ID")
user_id = st.text_input("Enter User ID")
if st.button("Get User"):
    st.write({"message": f"User ID received: {user_id}"})

# --- Search Employee ---
st.subheader("Search Employee")
name = st.text_input("Enter Name")
if st.button("Search"):
    st.write({"message": f"Searching for: {name}"})

# --- Get User Details ---
st.subheader("Get User Details")
detail_user_id = st.text_input("User ID")
show_email = st.checkbox("Show Email")
if st.button("Get Details"):
    st.write({
        "user_id": detail_user_id,
        "show_email": show_email
    })
