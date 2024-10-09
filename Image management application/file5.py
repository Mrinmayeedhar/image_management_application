@app.route('/download/<filename>')
def download_file(filename):
    file_obj = s3.get_object(Bucket='your-bucket-name', Key=filename)
    if 'decrypt' in request.args:
        decrypted_data = cipher.decrypt(file_obj['Body'].read())
        return decrypted_data
    else:
        return file_obj['Body'].read()