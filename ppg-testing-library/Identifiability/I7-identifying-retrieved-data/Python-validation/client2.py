#!/usr/bin/env python3

import requests

def get_data():
    url = 'http://other-domain.com/data'
    requests.get(url, params={"name": "name"})

if __name__ == '__main__':
    get_data()