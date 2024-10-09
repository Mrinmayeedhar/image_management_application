from flask import Flask, request
import boto3

app = Flask(_name_)
s3 = boto3.client('s3')

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        s3.upload_fileobj(file, 'imagescreatedbyme', file.filename)
        return 'Image uploaded successfully!'
    return '''
    <form method="post" enctype="multipart/form-data">
        <input type="file" name="file">
        <button type="submit">Upload</button>
    </form>
    '''