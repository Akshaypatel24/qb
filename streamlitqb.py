
import streamlit as st


st.title("QB app")

stars_bcbsm_url = "https://quillbot.com/"
st.write(
        f'<iframe src={stars_bcbsm_url} width="1500" height="600"></iframe>',
        unsafe_allow_html=True,
    )
