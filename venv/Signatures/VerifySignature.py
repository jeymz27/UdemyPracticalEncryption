import rsa


with open('docsender_publickey.pem', 'rb') as f:
    docsender_publickey = rsa.PublicKey.load_pkcs1(f.read())

with open('Testdocument.pdf', 'rb') as f:
    Testdocument = f.read()


#verifying the signature , we need the document that we want to verify , the signature file and the public key of the sender to the below function


with open('signature_file', 'rb') as f:
    signature_file = f.read()

verify_file = rsa.verify(Testdocument, signature_file, docsender_publickey)

print(verify_file)
