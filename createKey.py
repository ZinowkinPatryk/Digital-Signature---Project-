from Crypto.PublicKey import RSA
from Crypto.PublicKey import ECC
from certificate import createCertificate
from pathlib import Path

def createKey(algoritmChoosen="rsa"):
    ssh_dir = Path.home() / ".shh"
    ssh_dir.mkdir(parents=True, exist_ok=True)
    privateKey_path = ssh_dir / "privateKey.pem"
    match algoritmChoosen:
        case 'rsa':
            key = RSA.generate(2048) # mozna wspomniec o passphrase
            rsa_key = key.export_key(format="PEM", pkcs=8)
            with open(privateKey_path, "wb") as f:
                f.write(rsa_key)
            createCertificate(key.publickey().exportKey())
        case 'ecdsa':
            private_key = ECC.generate(curve='P-256')
            public_key = private_key.public_key().export_key(format='PEM')
            private_key = private_key.export_key(format='PEM')
            with open(privateKey_path, "wt") as f:
                f.write(private_key)
            createCertificate(public_key)
        case _:
            raise ValueError("Something went wrong")

if __name__ == "__main__":
    createKey("ecdsa")
