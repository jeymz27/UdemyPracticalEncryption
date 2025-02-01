import rsa
from u_basic_encryption import key

jeymz_pubkey,jeymz_privkey = rsa.newkeys(1024) #1024 is the length of the key, it could be bigger key as well.

# print("The Jeymz Pub key:",jeymz_pubkey) #The public key is used to encrypt the message
# print("The Jeymz Priv key:",jeymz_privkey)  #The private key is used to decrypt the message

#There are several formats to save the key file :
#1. PEM format
#2. DER format
#3. SSH format
#4. XML format

#The PEM format is the most common format for the key file. The key file is saved in the .pem file extension.
#The key file is saved in the .pem file extension.
#The key file is saved in the .der file extension.
#The key file is saved in the .pub file extension.
#The key file is saved in the .xml file extension.



# print("This is Jeymz Public Key RSA", jeymz_pubkey.save_pkcs1('PEM')) #The public key is saved in the PEM format
#
# print("This is Jeymz Public Key RSA decoded", jeymz_pubkey.save_pkcs1('PEM').decode()) #The public key is saved in the PEM format and decoded to get text output
#
# print("This is Jeymz Private Key RSA",jeymz_privkey.save_pkcs1('PEM')) #The private key is saved in the PEM format.
#
# print("This is Jeymz Private Key RSA decoded",jeymz_privkey.save_pkcs1('PEM').decode()) #The private key is saved in the PEM format and using the decode method to convert the key to text.

#testing my string for encoding and decoding with the keys :

# e_data = rsa.encrypt(b"Hello Jeymz",jeymz_pubkey) #The message is encrypted using the public key
# print("The encrypted data is:",e_data) #The encrypted data is displayed
#
# d_data = rsa.decrypt(e_data,jeymz_privkey) #The encrypted data is decrypted using the private key
# print("The decrypted data is:",d_data) #The decrypted data is displayed
# print("The decrypted data is:",d_data.decode()) #The decrypted data is displayed in text format

symmetric_key = key

def encript_symetric_key(symmetric_key):
    e_symmetric_key = rsa.encrypt(symmetric_key,jeymz_pubkey)
    return e_symmetric_key



def decript_symetric_key(e_symmetric_key):
    d_symmetric_key = rsa.decrypt(e_symmetric_key,jeymz_privkey)
    return d_symmetric_key

e_symmetric_key = encript_symetric_key(symmetric_key)
print("The encrypted symmetric key is:",e_symmetric_key)

d_symmetric_key = decript_symetric_key(e_symmetric_key)
print("The decrypted symmetric key is:",d_symmetric_key)









