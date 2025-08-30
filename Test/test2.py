#!/usr/bin/python3

import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "name":"Abdullah",
    "Age": 30 ,
    "user": 1
}

res = requests.post(url, json=data)
print("State", res.status_code)
print("responds", res.json())