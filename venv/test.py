from cryptography.fernet import Fernet

key = Fernet.generate_key()
print("The Key is: ",key)


print("Hello James")