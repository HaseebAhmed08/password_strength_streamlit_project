import streamlit as st
import re

st.set_page_config(page_title="Password Generator", layout="centered")

def password_check(password):
    feedback = []
    score = 0

    if len(password) >= 8:
        score += 1
    else:
        feedback.append('Password should be at least 8 characters long.')

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append('You must include both uppercase and lowercase letters.')

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append('You must include numbers (0-9).')

    if re.search(r'[~!@#$%^&*]', password):  # Corrected the regex
        score += 1
    else:
        feedback.append('You must include symbols like ~!@#$%^&*.')

    if score == 4:
        st.success('Your password is strong and fully active!')
    elif score == 3:
        st.info('Moderate password. Please consider adding more complexity.')
    else:
        st.error('Your password is weak.')

    if feedback:
        with st.expander('Here are tips to improve your password:'):
            for item in feedback:
                st.write(item)

st.title('Password Strength Web Application')
st.subheader('--: Check how strong your password is :--')

password = st.text_input('--: Please enter your password here :--', type='password', help='Enter a strong password')

if st.button('Check Password'):
    if password:
        password_check(password)
    else:
        st.warning('Please enter a password first.')