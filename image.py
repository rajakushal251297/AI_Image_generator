import openai
import streamlit as st
openai.api_key = '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'

try:
    user_command=str(st.text_input("AI GENERATED PHOTOS"))
    if st.button("Find/Next"):
        response = openai.Image.create(
        prompt=user_command,
        n=1,
        size="1024x1024"
        )
        image_url = response['data'][0]['url']
        st.image(image_url)
except Exception as e:
    st.write("Not Found or Connectivity Problem")






