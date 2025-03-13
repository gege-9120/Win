from cryptography.fernet import Fernet
import os

# Load the encryption key
with open("key.key", "rb") as f:
    key = f.read()

fernet = Fernet(key)

# Decrypt all files
for dirpath, _, filenames in os.walk(os.getcwd()):
    for filename in filenames:
        file_path = os.path.join(dirpath, filename)

        # Skip the key file and the decrypter itself
        if filename in ["key.key", "decrypter.py", "encrypter.py", "decrypter2.py", "encrypter.py"]:
            continue  

        try:
            with open(file_path, "rb") as f:
                encrypted_data = f.read()

            # Decrypt data
            decrypted = fernet.decrypt(encrypted_data)

            # Write decrypted data back
            with open(file_path, "wb") as f:
                f.write(decrypted)

            print(f"Decrypted: {file_path}")

        except Exception as e:
            print(f"Failed to decrypt {file_path}: {e}")
print("Decryption complete!")
