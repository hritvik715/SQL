# //imp-> flash-8b => ye vaala kaam kar rha hai

# //imp-> pehle virtual envirnmt activate karna hoga phir run karo tabb chalega
# //imp-> .\venv\Scripts\Activate.ps1
from dotenv import load_dotenv
load_dotenv()  ## load all the environment variables


import streamlit as st
import os
import sqlite3


import google.generativeai as genai

## Configure our API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))




## Function To Load Google Gemini Model and provide queries as response
# prompt jo line 41 mey hai vo ek list hai and hamne prompt[0] likha hai parameter mey  
def get_gemini_response(question,prompt):
    # model=genai.GenerativeModel('gemini-pro')
    # model=genai.GenerativeModel('models/gemini-1.5-flash-8b')
    model=genai.GenerativeModel('models/gemini-flash-latest')
    response=model.generate_content([prompt[0],question])
    return response.text




## Fucntion To retrieve query from the database

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## Define Your Prompt (ye prompt de rhe hai model ko ki kaise behave karna hai)
prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output

    """


]

## Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

# if submit is clicked
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    response=read_sql_query(response,"student.db")
    st.subheader("The Response is")
    for row in response:
        print(row)
        st.header(row)















# //imp-> 2nd way









# from dotenv import load_dotenv
# load_dotenv()  ## load all the environment variables

# import streamlit as st
# import os
# import sqlite3
# import time
# import random
# import re
# from google.api_core import exceptions as google_exceptions

# import google.generativeai as genai

# ## Configure our API key
# api_key = os.getenv("GOOGLE_API_KEY")
# if api_key:
#     # Remove any quotes or whitespace that might be in the .env file
#     api_key = api_key.strip().strip('"\'')
#     genai.configure(api_key=api_key)
# else:
#     st.error("API Key not found. Please check your .env file.")

# # Use session state for caching to persist between Streamlit refreshes
# if 'response_cache' not in st.session_state:
#     st.session_state.response_cache = {}

# ## Function To Load Google Gemini Model and provide queries as response
# def get_gemini_response(question, prompt, max_retries=5):
#     # Check if we already have this question in our cache
#     cache_key = question.strip().lower()  # Normalize the question for better cache hits
#     if cache_key in st.session_state.response_cache:
#         st.info("Using cached response")
#         return st.session_state.response_cache[cache_key]
    
#     # Try different models in case of issues
#     models_to_try = [
#         # 'models/gemini-1.5-pro',
#         'models/gemini-1.5-flash-8b',  # Try this as a fallback - usually has higher quotas
#         # 'models/gemini-1.0-pro'     # Another fallback
#     ]
    
#     last_error = None
#     for model_name in models_to_try:
#         for attempt in range(max_retries):
#             try:
#                 model = genai.GenerativeModel(model_name)
#                 response = model.generate_content([prompt[0], question])
#                 response_text = response.text
                
#                 # Store the successful response in cache for future use
#                 st.session_state.response_cache[cache_key] = response_text
#                 return response_text
                
#             except google_exceptions.ResourceExhausted as e:
#                 last_error = e
#                 if attempt < max_retries - 1:
#                     # Exponential backoff with jitter
#                     sleep_time = (2 ** attempt) + random.random()
#                     st.warning(f"Rate limit hit with {model_name}. Retrying in {sleep_time:.1f} seconds...")
#                     time.sleep(sleep_time)
#                 else:
#                     # Try next model if available
#                     break
#             except Exception as e:
#                 last_error = e
#                 break
    
#     st.error(f"All models failed. Last error: {str(last_error)}")
#     return f"SELECT 'Error: Could not generate SQL query. Please try again later.' AS message;"

# ## Determine if text is valid SQL
# def is_valid_sql(text):
#     # Check if the text starts with common SQL keywords
#     sql_pattern = r"^\s*(SELECT|INSERT|UPDATE|DELETE|CREATE|DROP|ALTER|WITH)\s+"
#     return re.match(sql_pattern, text, re.IGNORECASE) is not None

# ## Function To retrieve query from the database
# def read_sql_query(sql, db):
#     # Safety check - verify this looks like a SQL query
#     if not is_valid_sql(sql):
#         st.error(f"Invalid SQL query: {sql}")
#         return [("Invalid SQL query. Please try again.",)]
        
#     try:
#         conn = sqlite3.connect(db)
#         cur = conn.cursor()
#         cur.execute(sql)
#         rows = cur.fetchall()
#         conn.commit()
#         conn.close()
#         return rows
#     except Exception as e:
#         st.error(f"SQL Error: {str(e)}")
#         return [(f"Error executing query: {str(e)}",)]

# ## Define Your Prompt
# prompt = [
#     """
#     You are an expert in converting English questions to SQL query!
#     The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
#     SECTION, MARKS \n\nFor example,\nExample 1 - How many entries of records are present?, 
#     the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
#     \nExample 2 - Tell me all the students studying in Data Science class?, 
#     the SQL command will be something like this SELECT * FROM STUDENT 
#     where CLASS="Data Science"; 
#     \nExample 3 - What is the average marks of all students?,
#     the SQL command will be something like this SELECT AVG(MARKS) FROM STUDENT;
    
#     ONLY return the SQL query without any explanation or markdown formatting.
#     Do not include backticks or the word 'sql' in your response.
#     """
# ]

# ## Streamlit App
# st.set_page_config(page_title="I can Retrieve Any SQL query")
# st.header("Gemini App To Retrieve SQL Data")

# # Add an info section showing table schema
# with st.expander("Database Information"):
#     st.write("""
#     **Table:** STUDENT
    
#     **Columns:**
#     - NAME (VARCHAR)
#     - CLASS (VARCHAR)
#     - SECTION (VARCHAR)
#     - MARKS (INT)
    
#     **Example data:**
#     - Krish, Data Science, A, 90
#     - Sudhanshu, Data Science, B, 100
#     - Darius, Data Science, A, 86
#     - Vikash, DEVOPS, A, 50
#     - Dipesh, DEVOPS, A, 35
#     """)

# question = st.text_input("Input: ", key="input")

# # Add a clear cache button
# if st.button("Clear Cache"):
#     st.session_state.response_cache = {}
#     st.success("Cache cleared!")

# submit = st.button("Ask the question")

# # if submit is clicked
# if submit:
#     with st.spinner("Processing your question..."):
#         response = get_gemini_response(question, prompt)
        
#         # Show the generated SQL query in a code block
#         st.subheader("Generated SQL")
#         st.code(response, language="sql")
        
#         # Only execute if it looks like valid SQL
#         if is_valid_sql(response):
#             st.subheader("Results")
#             result = read_sql_query(response, "student.db")
            
#             # Display results in a more structured way
#             if result:
#                 if len(result[0]) > 1:  # Multiple columns
#                     st.table(result)
#                 else:  # Single column/value
#                     for row in result:
#                         st.write(row[0])
#             else:
#                 st.write("No results returned.")
#         else:
#             st.error("Invalid SQL generated. Please try a different question.")