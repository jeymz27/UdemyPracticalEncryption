from cryptography.fernet import Fernet

# -- This below code is generating a new key all the time and using it
            # key = Fernet.generate_key()
            # print("The Key is: ",key)
            # cipher = Fernet(key)
            # encrypted_text = cipher.encrypt(b'This is James Potluri')
            # print("The encrypted text is:", encrypted_text)
            # decrypted_text = cipher.decrypt(encrypted_text)
            # print("This is decrypted text and original text that was encrypted:" , decrypted_text)


# -- This below code is using a key which is already generated and stored in a file mykey.key

with open('mykey.key', 'rb') as k_file:
    key = k_file.read()


cipher = Fernet(key)

with open('james.txt', 'rb') as w_file:
    data = w_file.read()

encrypted_data = cipher.encrypt(data)

with open('encrypted-james.txt', 'wb') as e_file:
    e_file.write(encrypted_data)


with open('encrypted-james.txt', 'rb') as o_file:
    edata = o_file.read()

decrypted_data = cipher.decrypt(edata)

with open('decrypted-james.txt', 'wb') as d_file:
    d_file.write(decrypted_data)

