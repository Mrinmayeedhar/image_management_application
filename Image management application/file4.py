from cryptography.fernet import Fernet
import boto3

key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt_file(data):
    return cipher.encrypt(data)

@app.route('/', methods=['POST'])
def upload_file():
    file = request.files['file']
    if 'encrypt' in request.form:
        encrypted_data = encrypt_file(file.read())
        s3.put_object(Bucket='imagescreatedbyme', Key=file.filename, Body=encrypted_data)
    else:
        s3.upload_fileobj(file, 'imagescreatedbyme', file.filename)
    return 'File uploaded successfully'