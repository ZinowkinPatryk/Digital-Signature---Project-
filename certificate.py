import json
import base64
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from pathlib import Path
import datetime
def createCertificate(user_public_key):
    with open("ApplicationPrivateKey.pem", "rb") as f:
        app_private_key = RSA.import_key(f.read(), passphrase="m;QwAzzp<&RKf!41j5#")

    if isinstance(user_public_key, bytes):
        user_public_key = user_public_key.decode("utf-8")
    cert_data = {
        "public_key": user_public_key,
        "issuer": "Patryk Z, Igor Ł. podpis dokumentu"
    }
    cert_data_bytes = json.dumps(cert_data, sort_keys=True).encode('utf-8')
    hash_obj = SHA256.new(cert_data_bytes)
    signature = pkcs1_15.new(app_private_key).sign(hash_obj)
    certificate = {
        "data": cert_data,
        "signature": base64.b64encode(signature).decode('utf-8')
    }
    ssh_dir = Path.home () / ".ssh"
    ssh_dir.mkdir (parents=True, exist_ok=True)
    cert_path = ssh_dir / f"publicKey{datetime.datetime.now()}.json"
    with open(cert_path, "w") as f:
        json.dump(certificate, f, indent=4)


if __name__ == "__main__":
    createCertificate("publicKey.pem", "ApplicationPrivateKey.pem")
