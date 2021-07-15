# for more information read : https://support.sigfox.com/apidocs#
# import requests module
import requests
from requests.auth import HTTPBasicAuth
from sigfox_config import sigfox_c
import json
import datetime

device_id = sigfox_c["device_id"]
Login = sigfox_c["Login"]
Password = sigfox_c["Password"]


Device_retreive_a_list_of_message_url = "https://api.sigfox.com/v2/devices/"+device_id+"/messages"
# Making a get request
response = requests.get(Device_retreive_a_list_of_message_url,
            auth = HTTPBasicAuth(Login, Password))

# print request object
if (response != 200):
    exit

response = json.loads(response.text)["data"]

for resp in response:
    s = resp['time'] / 1000.0
    time = datetime.datetime.fromtimestamp(s).strftime('%Y-%m-%d %H:%M:%S')
    bytes_object = bytes.fromhex(resp['data'])
    data = bytes_object.decode("ASCII")
    print(time +' : '+ data)
