import streamlit as st
import re

def check_password_strength(password):
    strength = 0
    feedback = []

    # Length check
    if len(password) >= 12:
        strength += 1
    else:
        feedback.append("Make the password at least 12 characters long.")

    # Uppercase check
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Lowercase check
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Digit check
    if re.search(r'\d', password):
        strength += 1
    else:
        feedback.append("Include at least one number.")

    # Special character check
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        feedback.append("Use at least one special character (!@#$%^&* etc.).")

    # Password Strength Rating
    if strength == 8:
        return "Strong 💪", "green", []
    elif strength >= 5:
        return "Moderate 🟠", "orange", feedback
    else:
        return "Weak ❌", "red", feedback

# Streamlit UI
st.title("🔐 Password Strength Meter")
st.write("Enter a password below to check its strength.")

# Input field
password = st.text_input("Enter Password", type="password")

if password:
    strength, color, suggestions = check_password_strength(password)

    # Display Strength
    st.markdown(f"<h3 style='color:{color};'>Password Strength: {strength}</h3>", unsafe_allow_html=True)

    # Show Suggestions if needed
    if suggestions:
        st.warning("Suggestions to improve your password:")
        for suggestion in suggestions:
            st.write(f"✅ {suggestion}")
