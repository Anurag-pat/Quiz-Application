import mysql.connector
import random


db = mysql.connector.connect(host="localhost",user="root",password="anurag")

cursor = db.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS quiz_app")


cursor.execute("USE quiz_app")


cursor.execute("""
CREATE TABLE IF NOT EXISTS users (

    id INT AUTO_INCREMENT PRIMARY KEY,
    enrollment_number VARCHAR(20) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    name VARCHAR(50),
    email VARCHAR(50),
    phone VARCHAR(15),
    age INT,
    gender VARCHAR(10),
    address TEXT,
    city VARCHAR(50),
    state VARCHAR(50),
    country VARCHAR(50)

)
""")


cursor.execute("""

CREATE TABLE IF NOT EXISTS questions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    question_text TEXT NOT NULL,
    option1 VARCHAR(50),
    option2 VARCHAR(50),
    option3 VARCHAR(50),
    option4 VARCHAR(50),
    correct_option INT
)
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS results (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    score INT,
    FOREIGN KEY (user_id) REFERENCES users(id)
)
""")



def register():
    print("---------------------------------")
    print()
    print("Register New User")
    print()
    print("---------------------------------")
    enrollment_number = input("Enter your Enrollment Number: ")
    cursor.execute("SELECT * FROM users WHERE enrollment_number = %s", (enrollment_number,))
    if cursor.fetchone():
        print("Enrollment Number already exists. Please Enter the Different Enrollement Number:")
        return
    while(True):
            password=input("Enter the Password: ")
            length=len(password)
            l,u,d,s=0,0,0,0
            if(length>=8 and length<=20 ):
                for i in password:
                    if i.islower():
                        l+=1
                    if i.isupper():
                        u+=1
                    if i.isdigit():
                     d+=1
                    if (i in '@' or i in '#' or i in '%' or i in '_' or i in '$'):
                        s+=1
           
            if (l>=1 and u>=1 and d>=1 and s>=1):
                print("**************************************")
                print()
                print("You Password is Accepted")
                print()
                print("**************************************")
                
        
                break
            else:
                print("**************************************")
                print()
                print("Your Password is not Accepted")
                print()
                print("**************************************")
                
    name = input("Enter your Name: ").upper()
    while(True):
        email = input("Enter the Email: ")
        if email.endswith("@gmail.com"):
            print("**************************************")
            print()
            print("Email is accepted")
            print()
            print("**************************************")
    
            break
        else:
            print("**************************************")
            print()
            print("Your email is not accepted")
            print()
            print("**************************************")

    phone = input("Enter the Phone Number: ")
    while(True):
        print("""
                    ----------
                    ENTER AGE BETWEEN
                    AGE GREATER THAN OR EQUAL TO 15 AND
                    AGE LESS THAN OR EQUAL TO 80
                    ----------
            """)
        age = int(input("Enter Age(15-80): "))
        if (age>=15 and age<=80):
            print("**************************************")
            print()
            print("Age Accepted")
            print()
            print("**************************************")
            break
        else:
            print("**************************************")
            print()
            print("Age is not Accepted")
            print()
            print("**************************************")

    gender = input("Enter your Gender: ")
    address = input("Enter the Complete Address: ")
    city = input("Enter City Name: ")
    state = input("Enter State Name: ")
    country = input("Enter Country name: ")
    
    cursor.execute("""
        INSERT INTO users (enrollment_number, password, name, email, phone, age, gender, address, city, state, country)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (enrollment_number, password, name, email, phone, age, gender, address, city, state, country))
    db.commit() #Changes Reflect to database
    print("Registration Successful!")

    
def login():
    print("---------------------------------")
    print()
    print("User Login")
    print("---------------------------------")
    print()
    enrollment_number = input("Enrollment Number: ")
    password = (input("Password: "))
    
    cursor.execute("SELECT * FROM users WHERE enrollment_number=%s AND password=%s", (enrollment_number, password))
    user = cursor.fetchone()
    print(user)
    
    if user:
        print("Login Successful!")
        return user[0] 
    else:
        print("Invalid Enrollment Number or Password")
        return None
    
def insert_question():
    print("Add a New Question")
    question_text = input("Enter the question text: ")
    option1 = input("Option 1: ")
    option2 = input("Option 2: ")
    option3 = input("Option 3: ")
    option4 = input("Option 4: ")
    
    while True:
        try:
            correct_option = int(input("Enter the correct option number (1-4): "))
            if correct_option not in [1, 2, 3, 4]:
                print("Please enter a valid option number (1-4).")
            else:
                break
        except ValueError:
            print("Please enter a number (1-4).")
    
    cursor.execute("""
        INSERT INTO questions (question_text, option1, option2, option3, option4, correct_option)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (question_text, option1, option2, option3, option4, correct_option))
    db.commit()
    print("Question added successfully!")



def attempt_quiz(user_id):
    print("---------------------------------")
    print()
    print("Quiz Time!")
    print("---------------------------------")
    print()
    cursor.execute("SELECT * FROM questions")
    questions = cursor.fetchall()
    quiz_questions = random.sample(questions, 5)
    score = 0

    for question in quiz_questions:
        print("\n" + question[1])
        print("1. " + question[2])
        print("2. " + question[3])
        print("3. " + question[4])
        print("4. " + question[5])
        
        answer = int(input("Choose the correct option (1-4): "))
        
        if answer == question[6]:
            score += 1

    cursor.execute("INSERT INTO results (user_id, score) VALUES (%s, %s)", (user_id, score))
    db.commit()

def view_result(user_id):
    cursor.execute("SELECT score FROM results WHERE user_id=%s", (user_id,))
    results = cursor.fetchall()
    
    if results:
        print("Your Results:")
        for i, result in enumerate(results, start=1):
            print(f"Attempt {i}: Score - {result[0]}/5")
    else:
        print("No quiz attempts found.")

def update_password():
    prev_password=input("Enter the previous Password: ")
    cursor.execute("SELECT * FROM users WHERE password = %s", (prev_password,))
    user=cursor.fetchone()
    
    if user:
        while(True):
            new_password=input("Enter the New Password: ")
            length=len(new_password)
            l,u,d,s=0,0,0,0
            if(length>=8 and length<=20 ):
                for i in new_password:
                    if i.islower():
                        l+=1
                    if i.isupper():
                        u+=1
                    if i.isdigit():
                     d+=1
                    if (i in '@' or i in '#' or i in '%' or i in '_' or i in '$'):
                        s+=1
           
            if (l>=1 and u>=1 and d>=1 and s>=1):
                print("**************************************")
                print()
                print("You Password is Accepted")
                print()
                print("**************************************")
                break
            else:
                print("**************************************")
                print()
                print("Your Password is not Accepted")
                print()
                print("**************************************")
        enroll=input("Enter the enrollement Number: ")
        cursor.execute("SELECT * FROM users WHERE enrollment_number=%s AND password=%s" , (enroll,prev_password))
        usser = cursor.fetchone()
        if usser:
            cursor.execute("UPDATE users set password = %s where enrollment_number = %s",(new_password,enroll))
            db.commit()
            print()
            print("Your Password is Updated Successfully")
        else:
            print("Enter the Correct Enrollment Number: ")
    else:
        print()
        print("Enter correct prev_password")



def main():
    while True:
        print("\nQuiz Application")
        print("----------------------------------------------------------------------")
        print()
        print("1. Register")
        print("2. Login")
        print("3. Add Question")
        print("4. Exit")
        print()
        print("----------------------------------------------------------------------")
        choice = input("Choose an option: ")

        if choice == '1':
            register()
        elif choice == '2':
            user_id = login()
            if user_id:
                while True:
                    print("----------------------------------------")
                    print()
                    print("1. Attempt Quiz")
                    print("2. View Result")
                    print("3. Update Password")
                    print("4. Logout")
                    print()
                    print("----------------------------------------")
                    choice = input("Choose an option: ")

                    if choice == '1':
                        attempt_quiz(user_id)
                        
                    elif choice == '2':
                        view_result(user_id)
                    elif choice == '3':
                        update_password(user_id)
                    elif choice =='4':
                        break
                    else:
                        print("Invalid choice. Please try again.")
        elif choice == '3':
            insert_question()
        elif choice =='4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

cursor.close()
db.close()
