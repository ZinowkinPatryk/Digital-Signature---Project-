from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA, ECC
from Crypto.Signature import pkcs1_15
from Crypto.Signature import DSS


def verify_file(filepath="", signature="", keyPath=""):
    try:
        with open(filepath, "rb") as f:
            hash_code = SHA256.new(f.read())
    except FileNotFoundError:
        print("No such file or directory")
        return False

    try:
        with open(signature, "rb") as f_sig:
            signature = f_sig.read()
    except FileNotFoundError:
        print("No such file or directory")
        return False

    try:
        with open(keyPath, "rb") as f_key:
            key = f_key.read()
    except FileNotFoundError:
        print("No such file or directory")
        return False

    try:
        key = RSA.importKey(key)
        veri = pkcs1_15.new(key)
        algorithm = "rsa"
    except (ValueError, TypeError, IndexError):
        try:
            key =  ECC.import_key(key)
            veri = DSS.new(key, 'fips-186-3')
            algorithm = "ECDSA"
        except(ValueError, TypeError, IndexError):
            print("Error currupt public key ")
            return False
    try:
        veri.verify(hash_code, signature)
        return True
    except (ValueError, TypeError, IndexError):
        print("Signature verification failed")
        print("Maybe is some change in file")
        return False


if __name__ == "__main__":
    plik = "test.txt"
    podpis = "test.txt.sig"
    klucz_pub = "publicKey.pem"

    if verify_file(plik, podpis, klucz_pub):
        print("Verified file")

