import random as ran
users={}
quiz_questions=[
    {"question": "In which year was the Python language developed?", "choices": ["1. 1991", "2. 1985", "3. 1885"], "answer": 1},
    {"question": "In which language is Python written?", "choices": ["1. Java", "2. C", "3. PHP"], "answer": 2},
    {"question": "Which one of the following is the correct extension of the Python file?", "choices": ["1. .python", "2. .p", "3. .py"], "answer": 3},
    {"question": "Single Line comments in Python begin with Symbol", "choices": ["1. #", "2. @", "3. %"], "answer": 1},
    {"question": "Which of the Following are the fundamental building block of python Programming", "choices": ["1. Constants", "2. Tokens", "3. Identifiers"], "answer": 2},
    {"question": "The reserved words used by Pyhton Interpreter to recognize the structure of the Program are termed as", "choices": ["1. Tokens", "2. Literals", "3. Keywords"], "answer": 3},
    {"question": "What can be the maximum possible length of the Identifier", "choices": ["1. 31", "2. 79", "3. None of these"], "answer": 3},
    {"question": "Which of the following statement is correct about List", "choices": ["1. List can contain value of mixed data type", "2. A List with no element is called empty List", "3. All of these"], "answer": 3},
    {"question": "Which opperator can be used with List", "choices": ["1. in", "2. not in", "3. both (1) & (2)"], "answer": 3},
    {"question": "Which of the following commands will create a list", "choices": ["1. List=list()", "2. List1=[]", "3. All of these"], "answer": 3},
    {"question": "What is the use of append() function in list", "choices": ["1. It adds an items to the end of the list", "2. It adds an item anywhere in list", "3. It adds an items to the beginning of the list"], "answer": 1}
]
current_user=None
Score=0
while(True):
    print(
        """
        *******************************************************************************
                    1.Registration
                    2.View Users
                    3.Login
                    4.Attempt Quiz
                    5.Result
                    6.Exit
        *******************************************************************************
        """
    )
    oper=input("Enter the Operation: ")
    print()

    if oper=='1':
        print("**********          Register Yourself          **************\n")
        username=input("Enter the user name: ").upper()
        
        print("""
              
              Your Password Should Contain

                    1. 1 lower case letter
                    2. 1 upper case letter
                    3. 1 digit
                    4. 8 > length < 20
                    5. 1 special character except (@#%_$)
              
                """)
        while(True):
            userpassword=input("Enter the Password: ")
            length=len(userpassword)
            l,u,d,s=0,0,0,0
            if(length>=8 and length<=20 ):
                for i in userpassword:
                    if i.islower():
                        l+=1
                    if i.isupper():
                        u+=1
                    if i.isdigit():
                     d+=1
                    if (i in '@' or i in '#' or i in '%' or i in '_' or i in '$'):
                        s+=1
            if(username in users):
                print()
                print("**********************************************")
                print("You have Already Registerd")
                print("**********************************************")
                break
            elif (l>=1 and u>=1 and d>=1 and s>=1):
                print()
                print("**********************************************")
                print("You Password is Accepted")
                print("**********************************************")
                users[username]=userpassword
                print()
                print("**********************************************")
                print("Registration Successfully")
                print("**********************************************")
                break
            else:
                print("**********************************************")
                print("Your Password is not Accepted")
                print("**********************************************")
            
    
    elif oper=='2':
        print(list(users))
        
    elif oper=='3':
        print("**********          Login          **********\n")

        print("****************************************************************")
        username=input("Enter the User Name: ").upper()
        password=input("Enter the Password: ")
        print("****************************************************************")
        if len(users)==0:
            print()
            print("**********************************************")
            print("You have not yet Registed")
            print("Please Registered first")
            print("**********************************************")
        elif username in users and users[username]==password:
            current_user = username
            print()
            print("**********************************************")
            print(print(f"Login successful! Welcome, {username}"))
            print("**********************************************")
        else:
            print()
            print("**********************************************")
            print("Invalid User Name and Password")
            print("**********************************************")
    
    elif oper=='4':
        print("**********          Attempt Quize          **********\n")
        if current_user:
            selected_question=ran.sample(quiz_questions,5)
            score = 0
            print(f"{current_user}, let's start the quiz!\n")
            for i, question in enumerate(selected_question):
                print(f"Q{i+1}: {question['question']}")
                for choice in question['choices']:
                    print(choice)
                answer = int(input("Choose the correct answer (1, 2, or 3): "))
                if answer == question['answer']:
                    score += 1
            print()
            print("**********************************************")
            print("Quiz completed!")
            print("**********************************************")
            print()
            print("**********************************************")
            print(f"{current_user} check your result by pressing 5")
            print("**********************************************")
        else:
            print()
            print("**********************************************")
            print("You need to log in first to attempt the quiz.")
            print("**********************************************")
    
    elif oper=='5':
        print("**********          Result          **********\n")
        if current_user:
            print()
            print("**********************************************")
            print(f"{current_user}'s score: {score}/{len(selected_question)}")
            print("**********************************************")
        else:
            print()
            print("**********************************************")
            print("Please log in and attempt the quiz first.")
            print("**********************************************")

    elif oper=='6':
        break

    else:
        print("""
                    Invalid Choice
                    Please Enter the Valid Choice
                """)