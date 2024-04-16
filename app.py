from openai import OpenAI
import streamlit as st
f=open("D:/.openai_api_key.txt")

key=f.read()
st.snow()
st.title("GenAI App - AI Code Reviewer")
client=OpenAI(api_key=key)
prompt =st.text_area("enter code here")
if st.button("Generate")== True:
    st.balloons()
    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "user", "content": """You are a code debugging assistant. Your task is to help developers and identify the erros in the prompt"""},
        {"role": "user", "content": prompt}
      ]
)
if response.choices:

    st.write(response.choices[0].message.content)