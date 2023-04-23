import streamlit as st

title = '<p style="font-family:sans-serif; color:#7eb400; font-size: 42px;"><b>Driver License Checker</b></p>'


def main():
    st.markdown(
        f"""
         <style>
         .stApp {{
             background-image: url("https://shorturl.at/dhrxT");
             background-attachment: fixed;
             background-size: cover;
         }}
         </style>
         """,
        unsafe_allow_html=True
    )


st.markdown(title, unsafe_allow_html=True)

f1 = "Please type 'yes' if driver license is present, 'no' if missing: "


check = st.text_input(f1)

if check == "yes":
    st.text('User  allowed to drive')

if check == "no":
    st.text('User not allowed to drive')
if check != "no" and check != 'yes' and check != "":
    st.text('Command not recognized')


if __name__ == '__main__':
    main()
