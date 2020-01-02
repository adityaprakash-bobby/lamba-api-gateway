import json

movies = {
    'action': 'Desperado (1995)',
    'fantasy': 'Inception (2010)',
    'animated': ' Peter Pan (1953)',
    'western': 'The Good, the Bad and the Ugly (1966)',
    'superhero': 'The Dark Knight (2008)',
    'musical': 'The Rocky Horror Picture Show (1975)',
    'crime': 'Pulp Fiction (1994)',
    'comedy': 'The Naked Gun: From the Files of Police Squad! (1988)',
    'adventure': 'Raiders of the Lost Ark (1981)',
    'war': 'The Guns of Navarone (1961)',
    'guy': 'The Expendables (2010)',
    'romance': 'True Romance (1993)',
    'thriller': 'Psycho (1960)',
    'horror': 'Black Swan (2010)',
}

def lambda_handler(event, context):
    print(event)
    
    if event.get('httpMethod') == 'PUT':
        response = putMovie(event)
        return done(reponse)
    elif event.get('httpMethod') == 'GET':
        response = getMovie(event)
        return done(response)
        
def getMovie(event):
    
    genre = event['pathParameters']['genre']
    print(genre)
    return movies[genre]

def done(response):
    
    return {
        'statusCode': 200,
        'body': json.dumps(response),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Methods': '*',
            'Access-Control-Allow-Origin': '*'
        }
    }
