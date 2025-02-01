import rsa

with open('docsender_privatekey.pem', 'rb') as f:
    docsender_privatekey = rsa.PrivateKey.load_pkcs1(f.read())

with open('Testdocument.pdf', 'rb') as f:
    Testdocument = f.read()


#creating a signature file , we need the document that we want to sign , the private key of the sender and the hash value of the document to the below function

signature_file = rsa.sign(Testdocument, docsender_privatekey, 'SHA-256')
print("This is the signature:",signature_file.hex())
print("This is the length of the signature:",len(signature_file.hex()))

with open('signature_file', 'wb') as f:
    f.write(signature_file)



