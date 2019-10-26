import requests
import urllib


URL = "https://172.16.1.1:8090/login.xml"
r = requests.post(URL, data = {'password':'Password','username':'Username', 'mode':'191'}, verify=False)
