
from app import *

# question1="How many students are there in class 5?"
question1="Show all student names and their marks that are there in section A of class 5 and have scored above 90?"
print(question1)
response = get_model_response(question1, prompt)
print(response)
output_data=read_sql(response, "student.db")
for row in output_data:
    print(row)    