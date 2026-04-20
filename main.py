from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

secret_code = "Unguessable"
key = RSA.generate(2048)
encrypted_key = key.export_key(passphrase=secret_code, pkcs=1, prot_params={'iteration_count':131072})

with open("rsa_key.pem", "wb") as f:
    f.write(encrypted_key)

print(key.publickey().exportKey())

with open("test1.txt", "rb") as f:
    test = SHA256.new(f.read())
    print(test.hexdigest())

