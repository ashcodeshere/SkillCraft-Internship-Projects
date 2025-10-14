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

n=int(input("Enter task to be done: "))
if n==1:
    CipherText=SimpleToCipher()
    print(f"CipherText = {CipherText}")

else:
    print("Not a valid Task Number. ")