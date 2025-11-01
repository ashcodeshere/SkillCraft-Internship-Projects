# Build a tool that assesses the strength of a password based on criteria such as length, 
# presence of uppercase and lowercase letters, numbers and special case characters.

import re

def assess_password_strength(passwd):
    length=len(passwd)>=8
    uppercase=bool(re.search(r'[A-Z]',passwd))
    lowercase=bool(re.search(r'[a-z]',passwd))
    number=bool(re.search(r'[0-9]',passwd))
    specialchar=bool(re.search(r'[\W_]',passwd))
    score=sum([length,uppercase,lowercase,number,specialchar])
    strength=""
    if score==5:
       strength="Very Strong"
    elif score==4:
        strength="Strong"
    elif score==3:
       strength="Moderate"
    elif score==2:
        strength="Weak"
    elif score==1:
        strength="Very Weak"
    feedback=[]
    if not length:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase:
        feedback.append("Add at least one UpperCase Letter.")
    if not lowercase:
        feedback.append("Add at least one LowerCase Letter.")
    if not number:
        feedback.append("Include at least one number.")
    if not specialchar:
        feedback.append("Add at least one Special Character.")
    
    return{
        "Password":passwd,
        "Strength":strength,
        "Score (Out of 5)":score,
        "Feedback":feedback if feedback else ["Your password meets all recommended criteria! "]
    }

if __name__=="__main__":
    user_passwd=input("Enter your Password: ")
    if not user_passwd:
        print("No Password Entered")
    else:
        result=assess_password_strength(user_passwd)
        print("\nPassword Strength Assessment: ")
        print(f"Password: {result['Password']}")
        print(f"Strength: {result['Strength']}")
        print(f"Score: {result['Score (Out of 5)']}")
        print(f"Feedback:")
        for i in result['Feedback']:
            print(f"-> {i}")
