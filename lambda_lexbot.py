import json

def endpoint(event, context):
  return {
    'statusCode': 200,
    'body': json.dumps('This is a test response.')
  }
