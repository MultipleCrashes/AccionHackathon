import bottle 
import json
from bottle import route
import requests
from bottle import request , response 
import clearbit

# Full cont api key 
API_KEY = '3f2ac32ec8e14acc'
# Clear bit api key 
clearbit.key = 'sk_bf2dd1730dc953c3bb0f71beca8e6390'

# Sample GET request - http://127.0.0.1:8000/profile/emailid=inimitableharish@gmail.com

@route('/profile/<emailid>')
def get_profile_email(emailid):
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

@route('/profile/<mobileno>')
def get_profile_mobile(mobileno):
    headers = '''{"X-FullContact-APIKey":"''' + str(API_KEY) + '''"}'''
    mobile_info_api = 'https://api.fullcontact.com/v2/person.json?phone='
    mobile = str(mobileno.split('=')[1])
    get_api = mobile_info_api + mobile
    mobile_related_info = requests.get(get_api, headers=json.loads(headers))
    return json.loads(mobile_related_info.text)

if __name__ == '__main__':
    bottle.run(host='127.0.0.1',port=8000)
