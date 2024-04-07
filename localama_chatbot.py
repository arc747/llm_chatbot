from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import ollama

import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()


prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a useful assistant that answers to any queries"),
    ("user", "query: {query}")
    ])


st.title("Ollama-llama2_chatbot1")
input_text=st.text_input("Ask me anything..")

llm = Ollama(model="llama2")
output_parser = StrOutputParser()

chain = prompt|llm|output_parser


if input_text:
    st.write(chain.invoke({"query": input_text}))