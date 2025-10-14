#Task - Create a program that can encrypt and decrypt text using the Ceaser Cipher Algorithm.
# Allow users to input a message and a shift value to perform encryption and decryption

print(f"{'-'*50} Welcome {'-'*50}\n")
print("Enter specified number for task to perform\n")
print("1. Convert Simple text to Cipher text\n")
print("2. Convert Cipher text to Simple text\n")
print("3. Find  Shift Value\n")

def SimToCip():
    SimpleText=input("Enter Simple Text: ")
    ShiftVal=int(input("Enter Shift Value: "))
    for i in SimpleText:
        cipherval=(i+ShiftVal)
    return cipherval

n=int(input("Enter task to be done: "))
if n==1:
    CipherText=SimToCip()
    print(f"CipherText={CipherText}")
