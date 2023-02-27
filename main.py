import streamlit as st
# from gpt_index import GPTTreeIndex
import openai
import os
import streamlit.components.v1 as components
from llama_index import SimpleDirectoryReader, GPTSimpleVectorIndex

st.secrets.load_if_toml_exists()
openai.api_key = st.secrets["openai_api_key"]
# openai.organization = st.secrets["openai_organization"]
assert openai.api_key is not None, "OpenAI API key not found"
os.environ["OPENAI_API_KEY"] = openai.api_key
# os.environ["OPENAI_ORGANIZATION"] = openai.organization
st.title("Ask any question about the BP Energy Outlook 2023")

# load from disk
index = GPTSimpleVectorIndex.load_from_disk('index.json')

# input box
user_input = st.text_input("You", "What are the major updates in 2023 report comparing to 2022?")
# button
if st.button("Send"):
    # display user input
    st.write("You: " + user_input)
    # display clone response
    response = index.query(user_input)
    print("yo", dir(response))
    print(response)
    st.write("chatbot: " + str(response))

components.html(
    """
<script>
const doc = window.parent.document;
buttons = Array.from(doc.querySelectorAll('button[kind=primary]'));
const send = buttons.find(el => el.innerText === 'Send');
doc.addEventListener('keydown', function(e) {
    switch (e.keyCode) {
        case 13:
            send.click();
            break;
    }
});
</script>
""",
    height=0,
    width=0,
)

# add a reference to the source code at https://github.com/jiweiqi/energy-outlook-chatbot
st.markdown(
    """
    [Source code](https://github.com/jiweiqi/energy-outlook-chatbot)
    """
)

# reference to gpt-index
st.markdown(
    """
    Built with the amazing [GPT-Index](https://github.com/jerryjliu/gpt_index) library
    """
)
