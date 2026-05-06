from Crypto.PublicKey import RSA
from Crypto.PublicKey import ECC
from certificate import createCertificate

def createKey(algoritmChoosen="rsa"):
    match algoritmChoosen:
        case 'rsa':
            key = RSA.generate(2048) # mozna wspomniec o passphrase
            rsa_key = key.export_key(format="PEM", pkcs=8)
            with open("privateKey.pem", "wb") as f:
                f.write(rsa_key)
            createCertificate(key.publickey().exportKey())
        case 'ecdsa':
            private_key = ECC.generate(curve='P-256')
            public_key = private_key.public_key().export_key(format='PEM')
            private_key = private_key.export_key(format='PEM')
            with open("privateKey.pem", "wt") as f:
                f.write(private_key)
            createCertificate(public_key)
        case _:
            raise ValueError("Something went wrong")

if __name__ == "__main__":
    createKey("ecdsa")
