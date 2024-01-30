import mysql.connector

#FUNCTION TO SHOW TABLE
def showTable(tableName):
    myDatabase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Password",
    database = "school"
    )

    cursor = myDatabase.cursor()
    cursor.execute("SELECT * FROM " + tableName)
    result = cursor.fetchall()
    for x in result:
      print(x)

#MYSQL CREDENTIALS
myDatabase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Wolf@369",
    database = "school"
)

cursor = myDatabase.cursor()

#CREATING TABLE NAMED STUDENT
cursor.execute("CREATE TABLE student(studentId INT(5), firstName VARCHAR(20), lastName VARCHAR(20), age INT(2), grade FLOAT)")

#INSERTING SOME RANDOM VALUES
sql = "INSERT INTO student VALUES(%s, %s, %s, %s, %s)"
val = [
    (1, 'John', 'Doe', 20, 75.5),
    (2, 'Jane', 'Smith', 22, 82.3),
    (3, 'Bob', 'Johnson', 21, 68.9),
    (4, 'Alice', 'Williams', 23, 90.2),
    (5, 'Charlie', 'Brown', 19, 79.8)
    ]

cursor.executemany(sql, val)
myDatabase.commit()
print("RANDOM VALUES INSERTED")

showTable('student')
print('.')

#INSERTING SPECIFIC VALUE
valSpecific = (6, 'Alice', 'Smith', 18, 95.5)

cursor.execute(sql, valSpecific)
myDatabase.commit()
print("SPECIFIC VALUE INSERTED")

showTable('student')
print('.')

#UPDATING THE GRADE
sqlUpdate = "UPDATE student SET grade = 97.0 WHERE firstName = 'Alice'"

cursor.execute(sqlUpdate)
myDatabase.commit()
print("VALUES UPDATED")

showTable('student')
print('.')

#DELETE THE RECORD
sqlDelete = "DELETE FROM student WHERE lastName = 'Smith'"

cursor.execute(sqlDelete)
myDatabase.commit()
print("RECORD DELETED")

showTable('student')
print('.')

#SHOWING ALL THE RECORDS
print("ALL THE RECORDS ARE : ")
showTable('student')




