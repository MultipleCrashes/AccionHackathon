import bottle 
import json
from bottle import route
import requests
from bottle import request , response 
import clearbit

# Full cont api key 
API_KEY = ''
# Clear bit api key 
clearbit.key = ''

# Sample GET request - http://127.0.0.1:8000/profile/emailid=inimitableharish@gmail.com

@route('/profile/<emailid>')
def get_profile(emailid):
    '''Gets details of a person'''
    # FC 
    headers = '''{"X-FullContact-APIKey":"''' + str(API_KEY) + '''"}'''
    email_info_api = 'https://api.fullcontact.com/v2/person.json?email='
    email = str(emailid.split('=')[1])
    get_api = email_info_api + email
    print 'Getting details for emailid -> ',email 
    person_details = requests.get(get_api, headers=json.loads(headers))
    # Clearbit
    try:
        clear_bit_info = clearbit.Enrichment.find(email=email, stream=True)
    except Exception as e:
        print '-->',str(e)
    import ast 
    fc_details = json.loads(person_details.text)
    cb_details = json.loads(json.dumps(clear_bit_info))
    fc_details.update(cb_details)
    return fc_details


if __name__ == '__main__':
    bottle.run(host='127.0.0.1',port=8000)
