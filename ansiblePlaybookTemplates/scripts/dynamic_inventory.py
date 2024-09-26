#!/usr/bin/env python

import json
import requests

def get_hosts():
    response = requests.get('http://api.example.com/hosts')
    return response.json()

if __name__ == "__main__":
    inventory = {
        "web_servers": {
            "hosts": get_hosts()
        }
    }
    print(json.dumps(inventory))

