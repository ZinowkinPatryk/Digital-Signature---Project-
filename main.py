from Crypto.PublicKey import ECC
from Crypto.Hash import SHA256
from Crypto.Protocol.KDF import scrypt

# 1. Nasze hasło źródłowe (seed)
haslo = b"Moje_super_tajne_zdanie_z_ktorego_powstanie_klucz"

# 2. Bezpieczna derywacja klucza (zamiana hasła na 32 bajty)
# Używamy scrypt, aby zabezpieczyć się przed atakami brute-force
seed_32_bytes = scrypt(haslo, salt=b'stala_sol_aplikacji', key_len=32, N=2**14, r=8, p=1)

# 3. Konwersja bajtów na dużą liczbę całkowitą (wymóg algorytmu ECC)
d_int = int.from_bytes(seed_32_bytes, byteorder='big')

# 4. Ręczne skonstruowanie klucza prywatnego ECDSA (krzywa P-256)
private_key = ECC.construct(curve='P-256', d=d_int)
public_key = private_key.public_key()

print("Klucz prywatny został odtworzony z hasła!")
print(f"Klucz publiczny (hex): {public_key.export_key(format='SEC1').hex()[:60]}...")

