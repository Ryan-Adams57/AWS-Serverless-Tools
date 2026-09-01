import boto3, os, io
from PIL import Image
from datetime import datetime

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['METADATA_TABLE'])
RESIZED_BUCKET = os.environ['RESIZED_BUCKET']

def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        size = record['s3']['object']['size']

        response = s3.get_object(Bucket=bucket, Key=key)
        img = Image.open(io.BytesIO(response['Body'].read()))
        img.thumbnail((300, 300))

        buffer = io.BytesIO()
        img.save(buffer, format='JPEG')
        buffer.seek(0)
        resized_key = f"resized-{key}"
        s3.put_object(Bucket=RESIZED_BUCKET, Key=resized_key, Body=buffer)

        table.put_item(Item={
            'imageKey': key,
            'originalSize': size,
            'resizedKey': resized_key,
            'processedAt': datetime.utcnow().isoformat(),
            'dimensions': f"{img.width}x{img.height}"
        })
