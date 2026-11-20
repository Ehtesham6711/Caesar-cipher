🔐 Caesar Cipher

A simple and interactive Caesar Cipher Encryption and Decryption Application built using Python and Streamlit. This application allows users to encrypt and decrypt messages by shifting letters of the alphabet using a customizable shift key.

📌 Project Overview

The Caesar Cipher is one of the oldest and simplest encryption techniques. It works by shifting each letter in a message by a fixed number of positions in the alphabet.

This project provides a user-friendly web interface where users can enter a message, select a shift key, choose an operation (Encrypt or Decrypt), and generate the result instantly.

✨ Features
Text Encryption: Encrypt messages using the Caesar Cipher algorithm.
Text Decryption: Decrypt previously encrypted messages.
Custom Shift Key: Choose a shift value between 1 and 25.
Case Preservation: Maintains uppercase and lowercase letters.
Special Character Support: Preserves spaces, numbers, and special characters without modification.
Instant Results: Generate encrypted or decrypted output with a single click.
Download Result: Download the generated output as a .txt file.
Interactive UI: Simple and user-friendly interface powered by Streamlit.
🛠️ Technologies Used
Python – Core programming language.
Streamlit – Framework for building the interactive web application.
📂 Project Structure
text
Caesar-Cipher/
│
├── app.py              # Main Streamlit application
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation

⚙️ Installation and Setup

Follow these steps to run the project on your local machine.

1. Clone the Repository
bash
git clone https://github.com/your-username/Caesar-Cipher.git

2. Navigate to the Project Directory
bash
cd Caesar-Cipher

3. Install Dependencies
bash
pip install -r requirements.txt


If you don't have a requirements.txt file, install Streamlit directly:

bash
pip install streamlit

4. Run the Application
bash
streamlit run app.py

5. Open in Browser

Once the application starts, Streamlit will provide a local URL. Open it in your browser to access the Caesar Cipher application.

🚀 How to Use
Enter your message in the text area.
Select a shift key between 1 and 25 using the slider.
Choose an operation:
Encrypt: Convert your original message into encrypted text.
Decrypt: Convert encrypted text back into its original form.
Click the Generate Result button.
View the generated output.
Click Download Result to save the output as a text file.
🔍 Example

Input Message:

text
HELLO WORLD


Shift Key: 3

Operation: Encrypt

Output:

text
KHOOR ZRUOG


Decryption Example:

text
Input: KHOOR ZRUOG
Shift Key: 3
Operation: Decrypt
Output: HELLO WORLD

🧠 How the Caesar Cipher Works

The Caesar Cipher replaces each alphabetic character with another character shifted by a fixed number of positions.

Encryption Formula:

text
E(x) = (x + shift) % 26


Decryption Formula:

text
D(x) = (x - shift) % 26


Where:

x represents the numerical position of a letter in the alphabet (0–25).
shift represents the selected shift key.
% 26 ensures that the shifting wraps around the alphabet.
⚠️ Limitations
The Caesar Cipher is a basic encryption technique and is not suitable for protecting sensitive or confidential information.
It can be easily broken using brute-force attacks because there are only 25 possible non-zero shift keys.
It only transforms alphabetic characters; numbers, spaces, and special characters remain unchanged.
🔮 Future Improvements
Add support for automatic cipher detection.
Implement brute-force decryption.
Add support for encrypting and decrypting uploaded text files.
Improve the user interface with additional customization options.
Add more encryption algorithms, such as Vigenère Cipher.
👨‍💻 Author

Your Name

📜 License

This project is open-source and available for educational and learning purposes. Feel free to use, modify, and improve it.

⭐ If you find this project useful, consider giving the repository a star!
