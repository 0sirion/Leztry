import streamlit as st

st.title('DriverCheck')


def main():
    check = st.text_input(
        "Please type 'yes' if driver license is present, 'no' if missing: ")

    if check == "yes":
        st.text('User  allowed to drive')

        if check == "no":
            st.text('User not allowed to drive')
        else:
            st.text('Command not recognixsddzed')


if __name__ == '__main__':
    main()
