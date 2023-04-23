import streamlit as st

st.title('DriverCheck')


def main():
    check = st.text_input(
        'Please type 1 if river license is present, 0 if missing: ')

    if check == "1":
        st.text('User  allowed to drive')

        if check == "0":
            st.text('User not allowed to drive')
    else:
        st.text('Command not recognized')


if __name__ == '__main__':
    main()
