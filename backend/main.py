import bottle 
import json
from bottle import route
import requests

API_KEY = 'YourAPIKey' 

@route('/profile')
def get_profile():
    '''Gets details of person'''
    headers = '''{"X-FullContact-APIKey":"'''+str(API_KEY)+'''"}'''
    email_info_api = 'https://api.fullcontact.com/v2/person.json?email='
    email_id = 'inimitableharish@gmail.com'
    get_api = email_info_api + str(email_id)
    person_details = requests.get(get_api, headers=json.loads(headers))
    return json.loads(person_details.text)


if __name__ == '__main__':
    bottle.run(host='127.0.0.1',port=8000)
