import streamlit as st

st.title('DriverCheck')


def main():
    check = st.text_input(
        'Please type 1 if river license is present, 0 if missing: ')

    if check == "1":
        print('User  allowed to drive')

        if check == "0":
            print('User not allowed to drive')
    else:
        print('Command not recognized')


if __name__ == '__main__':
    main()
