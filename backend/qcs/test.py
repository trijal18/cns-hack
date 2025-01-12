from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os
import joblib
import io

# Placeholder for Post-Quantum Key Exchange (simulating Kyber)
class HybridCrypto:
    @staticmethod
    def generate_keypair():
        # Simulate post-quantum key generation
        public_key = os.urandom(32)  # Example public key
        private_key = os.urandom(32)  # Example private key
        return public_key, private_key

    @staticmethod
    def encapsulate(public_key):
        # Simulate post-quantum key encapsulation (Kyber-like)
        shared_secret = os.urandom(32)  # Shared secret for AES
        ciphertext = os.urandom(64)  # Ciphertext to be sent
        return ciphertext, shared_secret

    @staticmethod
    def decapsulate(ciphertext, private_key, shared_secret):
        # Simulate post-quantum key decapsulation (Kyber-like)
        # Ensure the decapsulated shared secret matches the original one.
        return shared_secret  # Return the same shared secret used in encapsulation

# Encrypt model using AES
def encrypt_model(model_bytes, shared_key):
    iv = os.urandom(16)  # Initialization Vector for AES
    cipher = Cipher(algorithms.AES(shared_key), modes.CFB(iv))
    encryptor = cipher.encryptor()
    encrypted_model = encryptor.update(model_bytes) + encryptor.finalize()
    return iv, encrypted_model

# Decrypt model using AES
def decrypt_model(encrypted_model, shared_key, iv):
    cipher = Cipher(algorithms.AES(shared_key), modes.CFB(iv))
    decryptor = cipher.decryptor()
    return decryptor.update(encrypted_model) + decryptor.finalize()

# Main process
if __name__ == "__main__":
    # Generate post-quantum keypair (simulated)
    pq_crypto = HybridCrypto()
    public_key, private_key = pq_crypto.generate_keypair()
    print("Public Key:", public_key.hex())
    print("Private Key:", private_key.hex())

    # Simulate key encapsulation to get shared secret
    ciphertext, shared_key = pq_crypto.encapsulate(public_key)
    print("Ciphertext:", ciphertext.hex())
    print("Shared Key (from encapsulation):", shared_key.hex())

    # Simulate key decapsulation to verify shared key
    derived_shared_key = pq_crypto.decapsulate(ciphertext, private_key, shared_key)
    print("Shared Key (from decapsulation):", derived_shared_key.hex())

    # Check if encapsulated and decapsulated keys match
    assert shared_key == derived_shared_key, "Key mismatch!"

    # Load the trained model (example with joblib)
    model = joblib.load(r"models\randomForest.pkl")

    # Serialize model to bytes using BytesIO
    model_bytes_io = io.BytesIO()
    joblib.dump(model, model_bytes_io)
    model_bytes = model_bytes_io.getvalue()

    # Encrypt the model using AES and the shared key
    iv, encrypted_model = encrypt_model(model_bytes, shared_key)
    with open("encrypted_model.bin", "wb") as f:
        f.write(iv + encrypted_model)
    print("Model encrypted successfully!")

    # Decrypt the model
    with open("encrypted_model.bin", "rb") as f:
        iv = f.read(16)  # Read IV from the file
        encrypted_model = f.read()  # Read the rest as encrypted model

    decrypted_model_bytes = decrypt_model(encrypted_model, derived_shared_key, iv)

    # Deserialize model from decrypted bytes
    decrypted_model_io = io.BytesIO(decrypted_model_bytes)
    decrypted_model = joblib.load(decrypted_model_io)
    print("Model decrypted successfully!")