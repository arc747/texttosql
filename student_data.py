import sqlite3

# connect to db
conn = sqlite3.connect("student.db")

# create a cursor object
cur = conn.cursor()

student_table = """create table student(ROLL_NO INT, NAME VARCHAR(25), CLASS VARCHAR(5), SECTION VARCHAR(2), MARKS INT)"""

cur.execute(student_table)

# insert records
cur.execute("""INSERT INTO STUDENT VALUES('2', 'Josh K', '5', 'A', 95)""")
cur.execute("""INSERT INTO STUDENT VALUES('1', 'Alice', '5', 'A', 90)""")
cur.execute("""INSERT INTO STUDENT VALUES('2', 'Bob', '6', 'B', 85)""")
cur.execute("""INSERT INTO STUDENT VALUES('3', 'Charlie', '7', 'C', 92)""")
cur.execute("""INSERT INTO STUDENT VALUES('4', 'David', '5', 'A', 88)""")
cur.execute("""INSERT INTO STUDENT VALUES('5', 'Emily', '6', 'B', 91)""")
cur.execute("""INSERT INTO STUDENT VALUES('6', 'Frank', '7', 'C', 89)""")
cur.execute("""INSERT INTO STUDENT VALUES('7', 'Grace', '5', 'A', 87)""")
cur.execute("""INSERT INTO STUDENT VALUES('8', 'Henry', '6', 'B', 93)""")
cur.execute("""INSERT INTO STUDENT VALUES('9', 'Isabel', '7', 'C', 86)""")
cur.execute("""INSERT INTO STUDENT VALUES('10', 'Jack', '5', 'A', 94)""")

print("Records inserted...")

data = cur.execute("""select * from student""")


print(data)

for row in data:
    print(row)
    
print(type(cur.fetchall()))

# commit and close the connection
conn.commit()
conn.close()


