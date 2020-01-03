import boto3
import asyncio

dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')
table = dynamodb.Table('movie-api')

class DB:
    def get(self, key, value, table):
        if not table:
            raise Exception('Table name needed.')
        if type(key) != str:
            raise Exception('Key was not a string.')
        if type(value) != str:
            raise Exception('Value was not a string.')

        try:
            response = table.get_item(
                Key={
                    key: value,   
                }
            )
        except Exception as e:
            print(f'There was error fetching data for {key} on table {table}')
        else:
            return reponse
            
    def write(self, ID, data, table):
        if not table:
            raise Exception('Table name needed.')
        if not data:
            raise Exception('Data needed.')
        if type(key) != str:
            raise Exception('Key was not a string.')
        
        try:
            result = table.put_item(
                Item={
                    data,
                    ID:ID
                }
            )
        except Exception as e:
            print('Could not write data into db.')
        else:
            return result
            
    async def increment(self, ID, table):
        pass
