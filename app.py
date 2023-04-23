import streamlit as st

title = '<p style="font-family:sans-serif; color:#7eb400; font-size: 42px;">Driver License Checker</p>'


def main():
    st.markdown(
        f"""
         <style>
         .stApp {{
             background-image: url("https://trafficlawfirm.com/wp-content/uploads/2019/05/How-Do-I-Check-if-My-License-Is-Suspended-in-Florida.jpg");
             background-attachment: fixed;
             background-size: cover;
         }}
         </style>
         """,
        unsafe_allow_html=True
    )


st.markdown(title, unsafe_allow_html=True)

check = st.text_input(
    "Please type 'yes' if driver license is present, 'no' if missing: ")

if check == "yes":
    st.text('User  allowed to drive')

if check == "no":
    st.text('User not allowed to drive')
if check != "no" and check != 'yes' and check != "":
    st.text('Command not recognized')


if __name__ == '__main__':
    main()
