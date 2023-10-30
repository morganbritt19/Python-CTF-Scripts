# This script will send a specified number of GET requests to a webserver to attempt to get the flag.txt file. This has been useful in some HackTheBox CTF events.

import requests

url = "http://[ip]:[port]/flag.txt"

for i in range(10):
    response = requests.get(url)
    print(f"Request {i+1}: Status code {response.status_code}")
    print(f"Response {i+1}: {response.text}")
