import streamlit as st
from embedings import ChromaEmbeddings
from llm_Interface import LLM_Interface



st.session_state.setdefault('results', [])

css = '''
<style>
.stTextLabelWrapper > div {
    text-wrap: wrap;
    white-space: break-spaces;
}
'''
st.write(css, unsafe_allow_html=True)

st.title('Test Playground')

def ask_question():
    question = st.session_state.question

    if not question:
        st.session_state.answer = 'Question is empty.'
        return

    rag_interface = ChromaEmbeddings()
    context = rag_interface.search(question)
    
    llm_interface = LLM_Interface()
    answer = llm_interface.ask_llm_with_context(question, context)

    st.session_state.results = answer

st.text_input(
    label='Type your question below',
    placeholder='Type your question here',
    key='question',
)

st.button(label='Ask Question', on_click=ask_question, use_container_width=True)

st.caption('Results:')

if len(st.session_state.results) == 0:
    st.text('No result')
else:
    # Display the results
    st.write(st.session_state.results)