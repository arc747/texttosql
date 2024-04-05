import os
import sqlite3
import streamlit as st
import google.generativeai as genai

from dotenv import load_dotenv
# load the env variables(API Key)
load_dotenv()

# access the API_KEY
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# load genmini pro model


def get_model_response(question, prompt):
    model = genai.GenerativeModel(model_name="gemini-pro")
    response = model.generate_content([prompt[0], question])
    return response.text

def read_sql(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    print(rows)
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows


prompt = [
    """
You are an expert in converting English questions to SQL query.
The SQL database name is student.db and has the student table with following columns: ROLL_NO, NAME, CLASS, SECTION, MARKS. \n\n
For Example, 
\nExample 1: How many records are there in the table?, the SQL command will be like 'select count(*) from student;',
\nExample 2: How many students are there in class 6?, the SQL command will be like 'select count(*) from student where class=6;',
\nExample 3: Show all students with marks greater than 90?, the SQL command will be like 'select roll_no, name, class, section, marks from student where marks>90;'
\n\n Also do not include the word sql or ''' at the beginning and end in the output sql query 
    """
    ]





st.set_page_config(page_title="Text to SQL results")
st.header("Gemini App to retrieve SQL data")
question=st.text_input("Input: ", key="input")
submit=st.button("ASk the question:")


if submit:
    response = get_model_response(question, prompt)
    print(question)
    print(response)
    output_data=read_sql(response, "student.db")
    st.subheader("Output: ")
    for row in output_data:
        print(row)
        st.header(row)
    


