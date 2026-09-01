import json, boto3, uuid, os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    method = event['httpMethod']
    path = event['path']

    if method == 'POST':
        body = json.loads(event['body'])
        item = {'id': str(uuid.uuid4()), 'task': body['task'], 'done': False}
        table.put_item(Item=item)
        return {'statusCode': 201, 'body': json.dumps(item)}

    elif method == 'GET' and path == '/todos':
        result = table.scan()
        return {'statusCode': 200, 'body': json.dumps(result['Items'])}

    elif method == 'GET':
        todo_id = event['pathParameters']['id']
        result = table.get_item(Key={'id': todo_id})
        return {'statusCode': 200, 'body': json.dumps(result.get('Item', {}))}

    elif method == 'DELETE':
        todo_id = event['pathParameters']['id']
        table.delete_item(Key={'id': todo_id})
        return {'statusCode': 200, 'body': json.dumps({'deleted': todo_id})}
