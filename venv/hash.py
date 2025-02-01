import rsa

message = b'Hello Jeymz Potluri - this is a test message for hashing'


hashedtext = rsa.compute_hash(message, 'SHA-512')
print(hashedtext.hex())

