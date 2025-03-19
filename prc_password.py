import streamlit as st
import re


st.set_page_config('password generator ',layout='centered')



def password_check(password):
    feedback = []
    score = 0

    if len(password)>=8:
        score =score +1

    else:
        feedback.append('password can be atleast 8 cheractors or greater then 8')


    if re.search(r'[A-Z]',password) and re.search(r'[a-z]',password):
        score = score +1

    else:
        feedback.append('you must add uper case & camel case letters in your password')

    if re.search(r'\d',password):
        score = score +1
    else:
        feedback.append('you must add numbers like 0 to 9')

    if re.search(r'~!@#$%^&*',password):
        score = score +1
    else:
        feedback.append['you must add symbol like ---->   ~!@#$%^&*']

    if score==4:
        st.success('apka password fully active an storng he')
    elif score == 3:
        st.info('modotrate password please continue at lea 8 cheracotrs')

    else:
        st.error('apke code me weak password set kia gaya he ')

st.title('password strength we Application')
st.subheader('--:  here you can ceck your password how much hard  :--')


password = st.text_input('--:  Please Enter your password Here  :--',type='password',help='Enter Correct Password')
