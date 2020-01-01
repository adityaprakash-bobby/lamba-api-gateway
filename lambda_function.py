import json

def lambda_handler(event, context):
    # print(event)
    if event['httpMethod'] == 'GET':
        return getItem(event)
    if event['httpMethod'] == 'POST':
        return createCart(event)

def getItem(event):
    item = {
        'description': 'A red sweater',
        'colour': 'red',
        'price': '2000',
    }
    
    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }

def createCart(event):
    print(event.get('body'))
    
    return {
        'statusCode': 200,
        'body': json.dumps('The cart was created.')
    }
