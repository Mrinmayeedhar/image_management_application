@app.route('/images')
def list_images():
    response = s3.list_objects_v2(Bucket='your-bucket-name')
    images = [obj['Key'] for obj in response.get('Contents', [])]
    return f"Images: {images}"