from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA, ECC
from Crypto.Signature import pkcs1_15
from Crypto.Signature import DSS


def hashing(filepath="", keyPath=''):
    with open(filepath, "rb") as f:
        hash_code = SHA256.new(f.read())
        print(hash_code.hexdigest())
        try:
            signature = encryption_hash(hash_code, keyPath)
            with open(filepath +".sig", "wb") as f_sig:
                f_sig.write(signature)
        except Exception as e:
            raise ValueError(f"Signature went wrong -> {e}")


def encryption_hash(hash_code, keyPath=''):
    with open(keyPath, "rb") as f:
        key = f.read()
    signer = None
    try:
        key = RSA.importKey(key)
        signer = pkcs1_15.new(key)
    except (ValueError, TypeError, IndexError):
        try:
            key = ECC.import_key(key)
            signer =  DSS.new(key, 'fips-186-3')
        except (ValueError, TypeError):
            raise ValueError("Invalid key file")
    return signer.sign(hash_code)


if __name__ == "__main__":
    hashing("test.txt", "privateKey.pem")
