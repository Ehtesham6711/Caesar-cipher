
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Caesar Cipher",
    page_icon="🔐",
    layout="centered"
)

# Title
st.title("🔐 Caesar Cipher")
st.caption("Encrypt and decrypt your messages securely.")

st.divider()

# Caesar Cipher function
def caesar_cipher(text, shift, mode):

    result = ""

    for char in text:

        if char.isalpha():

            base = ord('A') if char.isupper() else ord('a')

            position = ord(char) - base

            if mode == "Encrypt":
                new_position = (position + shift) % 26
            else:
                new_position = (position - shift) % 26

            result += chr(base + new_position)

        else:
            result += char

    return result


# Input message
message = st.text_area(
    "Enter your message",
    placeholder="Type your message here..."
)

# Shift key
shift = st.slider(
    "Select Shift Key",
    min_value=1,
    max_value=25,
    value=3
)

# Select operation
mode = st.radio(
    "Choose Operation",
    ["Encrypt", "Decrypt"],
    horizontal=True
)

# Process button
if st.button("Generate Result", use_container_width=True):

    if message.strip():

        result = caesar_cipher(message, shift, mode)

        st.success(f"{mode}ion Successful!")

        st.subheader("Output")

        st.code(result)

        st.download_button(
            "Download Result",
            data=result,
            file_name="cipher_result.txt"
        )

    else:
        st.warning("Please enter a message first.")
