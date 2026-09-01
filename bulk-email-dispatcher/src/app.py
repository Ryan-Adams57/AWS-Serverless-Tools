import boto3, os, json

ses = boto3.client('ses', region_name='us-east-1')
sns = boto3.client('sns')
SENDER = os.environ['SENDER_EMAIL']
TOPIC_ARN = os.environ['SNS_TOPIC_ARN']
RECIPIENTS = ["user1@example.com", "user2@example.com"]

def lambda_handler(event, context):
    results = []
    for recipient in RECIPIENTS:
        try:
            response = ses.send_email(
                Source=SENDER,
                Destination={'ToAddresses': [recipient]},
                Message={
                    'Subject': {'Data': 'Your Daily Update'},
                    'Body': {'Text': {'Data': 'Hello! This is your scheduled email.'}}
                }
            )
            results.append({'recipient': recipient, 'status': 'sent'})
        except Exception as e:
            results.append({'recipient': recipient, 'status': 'failed', 'error': str(e)})

    sns.publish(TopicArn=TOPIC_ARN, Message=json.dumps(results), Subject='Email Dispatch Summary')
    return {'statusCode': 200, 'body': json.dumps(results)}
