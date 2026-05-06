import json
import base64
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA, ECC
from Crypto.Signature import pkcs1_15
from Crypto.Signature import DSS

# kolejnosc:
# plik txt:
# 1. sciezka do pliku, 2. plik .sig, 3. klucz publiczny , 4. klucz publiczny od nas (ApplicationPublicKey.pem)
# plik pdf:


def verify_file(*args):
    if ".pdf" in args[0]:
        print("t")
    elif ".txt" in args[0]:
        try:
            with open(args[0], "rb") as f_file:
                hash_code = SHA256.new(f_file.read())
        except FileNotFoundError:
            raise ValueError("Somethin went wrong with orginal file")
        try:
            with open(args[1], "rb") as f_sig:
                signature = f_sig.read()
        except FileNotFoundError:
            raise ValueError("Somethin went wrong with signature file")
        try:
            with open(args[2], "rb") as f_key:
                file_key = json.loads(f_key.read())
                user_public_key = file_key["data"].get("public_key")
                signature_public = file_key.get("signature")
        except:
            raise ValueError("Invalid key -> is not in json format")
        try:
            with open(args[3], "rb") as f_key_app:
                key_app = RSA.importKey(f_key_app.read())
        except:
            raise ValueError("Something went wrong with app key load")
        cert_data_bytes = json.dumps(file_key["data"], sort_keys=True).encode('utf-8')
        cert_hash = SHA256.new(cert_data_bytes)
        cert_signature_bytes = base64.b64decode(signature_public)
        try:
            pkcs1_15.new(key_app).verify(cert_hash, cert_signature_bytes)
        except (ValueError, TypeError):
            raise ValueError("Certificate error")
        try:
            user_key_obj = RSA.import_key(user_public_key)
            veri = pkcs1_15.new(user_key_obj)
        except (ValueError, TypeError, IndexError):
            try:
                user_key_obj = ECC.import_key(user_public_key)
                veri = DSS.new(user_key_obj, 'fips-186-3')
            except (ValueError, TypeError, IndexError):
                raise ValueError("User key error")
        try:
            veri.verify(hash_code, signature)
            return True
        except (ValueError, TypeError):
            return False
    else:
        raise ValueError("Wrong file")


if __name__ == "__main__":
    plik = "test.txt"
    podpis = "test.txt.sig"
    klucz_pub = "publicKey.pem"

