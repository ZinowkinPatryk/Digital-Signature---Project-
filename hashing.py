from Crypto.Hash import SHA256


def hashing(filepath=""):
    with open(filepath, "rb") as f:
        hash_code = SHA256.new(f.read())
        print(hash_code.hexdigest())
        hash_code = encryption_hash()


def encryption_hash(hash_code='', keyPath=''):
    pass


if __name__ == "__main__":
    hashing("/Digital-Signature---Project-/test.txt")
