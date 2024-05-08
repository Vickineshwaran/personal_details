import mysql.connector
def connect_to_database():
 try:
 connection = mysql.connector.connect(
 host="localhost",
 user="username",
 password="password",
 database="databasename"
 )
 return connection
 except mysql.connector.Error as error:
 print("Failed to connect to MySQL:", error)
def add_person(connection, aadhaar_no, name, age, dob, blood_group, phone_no):
 try:
 cursor = connection.cursor()
 sql_query = "INSERT INTO person_details (aadhaar_no, name, age, dob, blood_group, 
phone_no) VALUES (%s, %s, %s, %s, %s, %s)"
 data = (aadhaar_no, name, age, dob, blood_group, phone_no)
 cursor.execute(sql_query, data)
 connection.commit()
 print("Person details added successfully!")
 except mysql.connector.Error as error:
 print("Failed to add person details:", error)
def search_person_by_aadhaar(connection, aadhaar_no):
 try:
 cursor = connection.cursor()
 sql_query = "SELECT * FROM person_details WHERE aadhaar_no = %s"
 cursor.execute(sql_query, (aadhaar_no,))
 result = cursor.fetchone()
 if result:
 print("Person details found:")
 print("Aadhaar No:", result[0])
 print("Name:", result[1])
 print("Age:", result[2])
 print("Date of Birth:", result[3])
 print("Blood Group:", result[4])
 print("Phone No:", result[5])
 else:
 print("Person with Aadhaar number {} not found.".format(aadhaar_no))
 except mysql.connector.Error as error:
 print("Failed to search person details:", error)
def delete_person_by_aadhaar(connection, aadhaar_no):
 try:
 cursor = connection.cursor()
 sql_query = "DELETE FROM person_details WHERE aadhaar_no = %s"
 cursor.execute(sql_query, (aadhaar_no,))
 connection.commit()
 print("Person details with Aadhaar number {} deleted 
successfully!".format(aadhaar_no))
 except mysql.connector.Error as error:
 print("Failed to delete person details:", error)
def create_table(connection):
 try:
 cursor = connection.cursor()
 cursor.execute("""
 CREATE TABLE IF NOT EXISTS person_details (
 aadhaar_no VARCHAR(12) PRIMARY KEY,
 name VARCHAR(255),
 age INT,
 dob DATE,
 blood_group VARCHAR(5),
 phone_no VARCHAR(15)
 )
 """)
 except mysql.connector.Error as error:
 print("Failed to create table:",error)
# Main function
def main():
 connection = connect_to_database()
 create_table(connection)
 if connection:
 while True:
 print("\n1. Add person details")
 print("2. Search person by Aadhaar number")
 print("3. Delete person by Aadhaar number")
 print("4. Exit")
 choice = input("Enter your choice: ")
 if choice == "1":
 aadhaar_no = input("Enter Aadhaar number: ")
 name = input("Enter name: ")
 age = int(input("Enter age: "))
 dob = input("Enter date of birth (YYYY-MM-DD): ")
 blood_group = input("Enter blood group: ")
 phone_no = input("Enter phone number: ")
 add_person(connection, aadhaar_no, name, age, dob, blood_group, phone_no)
 elif choice == "2":
 aadhaar_no = input("Enter Aadhaar number to search: ")
 search_person_by_aadhaar(connection, aadhaar_no)
 elif choice == "3":
 aadhaar_no = input("Enter Aadhaar number to delete: ")
 delete_person_by_aadhaar(connection, aadhaar_no)
 elif choice == "4":
 print("Exiting...")
 break
 else:
 print("Invalid choice!")
 connection.close()
main()
