#Task - Create a program that can encrypt and decrypt text using the Ceaser Cipher Algorithm.
# Allow users to input a message and a shift value to perform encryption and decryption

print(f"{'-'*50} Welcome {'-'*50}\n")
print("Enter specified number for task to perform\n")
print("1. Convert Simple text to Cipher text\n")
print("2. Convert Cipher text to Simple text\n")
print("3. Find  Shift Value\n")

def SimpleToCipher():
    SimpleText=input("Enter Simple Text: ")
    ShiftVal=int(input("Enter Shift Value: "))
    cipherval=""
    for i in SimpleText:
        if i.isalpha():
            start=ord('A') if i.isupper() else ord('a')
            cipherval+=chr((ord(i)-start+ShiftVal)%26+start)
        else:
            cipherval+=i            
    return cipherval

def CipherToSimple():
    CipherText=input("Enter Cipher Text: ")
    ShiftVal=int(input("Enter Shift Value: "))
    SimpleText=""
    for i in CipherText:
        if i.isalpha():
            start=ord('A') if i.isupper() else ord('a')
            SimpleText+=chr((ord(i)-start-ShiftVal)%26+start)
        else:
            SimpleText+=i
    return SimpleText

def ShiftValue():
    # To be defined soon
    return ShiftVal

n=int(input("Enter task to be done: "))
if n==1:
    CipherText=SimpleToCipher()
    print(f"CipherText = {CipherText}")
elif n==2:
    SimpleText=CipherToSimple()
    print(f"Simple Text = {SimpleText}")
elif n==3:
    ShiftVal=ShiftValue()
    print(f"Shift Value = {ShiftVal}")
else:
    print("Not a valid Task Number. ")