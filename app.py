import os
import io
import streamlit as st
import pandas as pd
from langchain.llms import OpenAI
from langchain.agents import create_pandas_dataframe_agent
from langchain.tools.python.tool import PythonREPLTool, PythonAstREPLTool

class CSVagent:
    def __init__(self, api_key, df):
        os.environ['OPENAI_API_KEY'] = api_key
        self.agent = create_pandas_dataframe_agent(OpenAI(temperature=0), df, verbose=True, max_iterations=2)

    def run(self, query):
        return self.agent.run(query)

def read_file(uploaded_file):
    if uploaded_file is not None:
        file_content = uploaded_file.read()
        file_type = uploaded_file.name.split('.')[-1]

        try:
            if file_type == 'csv':
                return pd.read_csv(io.StringIO(file_content.decode('utf-8')))
            elif file_type in ['xlsx', 'xls']:
                return pd.read_excel(io.BytesIO(file_content))
            elif file_type == 'json':
                return pd.read_json(io.StringIO(file_content.decode('utf-8')), lines=True)
            else:
                st.error(f"Unsupported file type: {file_type}. Please upload a CSV, Excel, or JSON file.")
                return None

        except Exception as e:
            st.error(f"An error occurred: {e}")
            return None

    else:
        st.info("Please upload a file.")
        return None


st.title("File Upload Pandas Viewer")
st.markdown("Upload a CSV, Excel, or JSON file to view its contents using pandas.")
uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx", "xls", "json"])

df = read_file(uploaded_file)

if df is not None:
    st.dataframe(df)

    st.warning("Please enter a query.")
    input_value = st.text_input("Enter a value", key="input")

    if input_value:
        try:
            AG = CSVagent('Your-OpenAI-API-Key', df)
            answer = AG.run(input_value)
            st.write("Answer:", answer)
        except Exception as e:
            st.error(f"An error occurred: {e}")
else:
    st.info("No valid DataFrame loaded.")