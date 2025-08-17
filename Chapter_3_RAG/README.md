## Introduction

Welcome to StackBuilder! 
In this chapter we will learn Retrieval-Augmented Generation (RAG) is very useful technique for AI based project development.

## Setup
We assume Setup of earlier chapters already completed.
For generating Vector embedding we need a embedding model, since we are on free tier of OpenAI we can not use OpenAI embedding model, so in this chapter we will use `GPT4All`.
GPT4All will allow us to download locally hosted embedding model.

### Adding Streamlit dependency
- Add `GPT4All` librancy under `requirements.txt` file.
- run `pip install -r requirements.txt`

### Running Streamlit UI
- Run `streamlit run ./Chapter_3_RAG/streamlit_main.py` , it will launch browser.
- In browser type your question and hit `Ask LLM` button.
