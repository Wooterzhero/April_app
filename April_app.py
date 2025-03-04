import streamlit as st
import random

# Title of the app
st.markdown("<h1 style='color:pink;'>Reasons I Love April ❤️</h1>", unsafe_allow_html=True)

# List of reasons
reasons = [
    "Her smile",
    "Her little treats",
    "Her Bostons (dogs)",
    "Her butt",  # Adjusted based on preferences
    "Her boobs",  # Adjusted based on preferences
    "Her laugh",
    "Her smile",
    "Her cutie butt",
    "The way she makes me feel",
    "Her kind heart"
]

# Initialize session state
if 'displayed_reason' not in st.session_state:
    st.session_state.displayed_reason = None
if 'click_count' not in st.session_state:
    st.session_state.click_count = 0
if 'ten_clicks_message_shown' not in st.session_state:
    st.session_state.ten_clicks_message_shown = False

# Function to display a reason
def display_reason():
    st.session_state.click_count += 1

    if st.session_state.click_count == 10 and not st.session_state.ten_clicks_message_shown:
        # Show the message only once after the 10th click
        st.session_state.displayed_reason = "That's a lot of reasons, huh? ❤️"
        st.session_state.ten_clicks_message_shown = True
    else:
        # After the 10th click, randomize as normal
        st.session_state.displayed_reason = random.choice(reasons)

# Button to trigger the display
st.button("Click Me! ❤️", on_click=display_reason)

# Display the reason
if st.session_state.displayed_reason:
    st.write(f"## {st.session_state.displayed_reason} ❤️")
else:
    st.write("Press the button... I dare you.")