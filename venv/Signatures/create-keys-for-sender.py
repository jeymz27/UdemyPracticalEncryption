import rsa


docsender_puiblickey, docsender_privatekey = rsa.newkeys(2048)

with open('docsender_publickey.pem', 'wb') as f:
    f.write(docsender_puiblickey.save_pkcs1('PEM'))

with open('docsender_privatekey.pem', 'wb') as f:
    f.write(docsender_privatekey.save_pkcs1('PEM'))




