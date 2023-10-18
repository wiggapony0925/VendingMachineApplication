import streamlit as st
import config


def main():

    st.set_page_config(
        page_title="Vending Machine calculation Application",
        page_icon='💵',
        layout='wide',
        initial_sidebar_state="collapsed",
        menu_items={
            "Get Help": "https://github.com/wiggapony0925/VendingMachineApplication",
            "Report a bug": "https://github.com/wiggapony0925/VendingMachineApplication",
            "About": "# this application's purpose is to calculate expenses with in your buisness to be organized."
        }

    )

    st.markdown("# Vending machine expense manager ✨")
    st.markdown('___')

    col1, col2 = st.columns(2)

    with col1:
        pass


if __name__ == "__main__":
    main()