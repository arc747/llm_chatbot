# from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI


import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGSMITH_TRACING_V2"]="true"
# GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")



prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a useful assistant and help by responding to any queries"),
    ("user", "Query:{query}")
    ])

st.title("Langchain-Gemini Chatbot_1")
input_text=st.text_input("Search anything..")

# llm = ChatOpenAI(model="gpt-4-0613")
llm = ChatGoogleGenerativeAI(model="gemini-pro", convert_system_message_to_human=True)
output_parser = StrOutputParser()

# Create a chain from the runnables
chain = prompt|llm|output_parser

# q1 = "Solar System"
# print(chain.invoke({"query": q1}))

if input_text:
    st.write(chain.invoke({"query": input_text}))