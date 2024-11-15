import time
import random
import os


user_data_file = "users.txt"
questions_file = "questions.txt"
results_file = "results.txt"


def register():
    print("\n--- Register ---")
    name = input("Enter your name: ")
    enrollment = input("Enter your enrollment number: ")
    while(True):
        email = input("Enter your email: ")
        if(email.endswith("@gmail.com")):
            print("Email Varified")
            break
        else:
            print("""           Invalid Email ID
                                Re-Enter the Email ID
                  """)
        
    print("""
              
              Your Password Should Contain

                    1. 1 lower case letter
                    2. 1 upper case letter
                    3. 1 digit
                    4. 8 > length < 20
                    5. 1 special character except (@#%_$)
              
                """)
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
                print()
                print("**********************************************")
                print("You Password is Accepted")
                print("**********************************************")
                print()
                print("**********************************************")
                print("Registration Successfully")
                print("**********************************************")
                break
            else:
                print("**********************************************")
                print("Your Password is not Accepted")

    with open(user_data_file, "a") as f:
        f.write(f"{enrollment},{password},{name},{email}\n")
    print("Registration successful!")


def login():
    print("\n--- Login ---")
    enrollment = input("Enter your enrollment number: ")
    password = input("Enter your password: ")

    
    with open(user_data_file, "r") as f:
        users = f.readlines()
        for user in users:
            user_data = user.strip().split(",")
            
            
            if len(user_data) == 4:
                stored_enrollment, stored_password, _, _ = user_data
                if stored_enrollment == enrollment and stored_password == password:
                    print("Login successful!")
                    return enrollment
            else:
                print(f"Invalid user data format: {user}")
    print("Invalid enrollment number or password!")
    return None



def load_questions():
    questions = []
    with open(questions_file, "r") as f:
        data = f.readlines()
        for line in data:
            question, *options, correct = line.strip().split(",")
            questions.append({
                "question": question,
                "options": options,
                "correct": correct
            })
    random.shuffle(questions)
    return questions


def attempt_quiz(enrollment):
    print("\n--- Quiz ---")
    questions = load_questions()
    correct_answers = 0
    total_questions = len(questions)
    
    start_time = time.time()
    for i, q in enumerate(questions, start=1):
        print(f"\nQ{i}: {q['question']}")
        for j, option in enumerate(q['options'], start=1):
            print(f"{j}. {option}")
        
        answer = input("Your answer (1-3): ")
        if q['options'][int(answer) - 1] == q['correct']:
            correct_answers += 1
    
    end_time = time.time()
    time_taken = round(end_time - start_time, 2)
    score = f"{correct_answers}/{total_questions}"

    
    with open(results_file, "a") as f:
        f.write(f"{enrollment},{score},{time_taken} seconds\n")
    
    print(f"\nQuiz finished! Your score: {score}")
    print(f"Time taken: {time_taken} seconds")



def view_result(enrollment):
    print("\n--- Results ---")
    with open(results_file, "r") as f:
        results = f.readlines()
        found = False
        for result in results:
            result_data = result.strip().split(",")
            
            if len(result_data) == 3:
                result_enrollment, score, time_taken = result_data
                if result_enrollment == enrollment:
                    print(f"Score: {score}, Time: {time_taken}")
                    found = True
            else:
                print(f"Invalid result data format: {result}")
        
        if not found:
            print("No result found for this enrollment!")



def main():
    if not os.path.exists(user_data_file):
        open(user_data_file, 'w').close()  
    if not os.path.exists(questions_file):
        
        with open(questions_file, 'w') as f:
            f.write("In which year was the Python language developed?,1991,1985,1885,1991\n")
            f.write("In which language is Python written?,Java,C,PHP,C\n")
            f.write("Which one of the following is the correct extension of the Python file?,#,@,%,#\n")
            f.write("Single Line comments in Python begin with Symbol?,.python,.py,.p,.py\n")
    
    while True:
        print("\n--- Quiz Application ---")
        print("1. Register")
        print("2. Login")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            register()
        elif choice == '2':
            enrollment = login()
            if enrollment:
                while True:
                    print("\n1. Attempt Quiz")
                    print("2. View Results")
                    print("3. Logout")
                    sub_choice = input("Enter your choice: ")
                    if sub_choice == '1':
                        attempt_quiz(enrollment)
                    elif sub_choice == '2':
                        view_result(enrollment)
                    elif sub_choice == '3':
                        break
                    else:
                        print("Invalid choice!")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
