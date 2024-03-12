import http.client
import json

conn = http.client.HTTPSConnection("jsonplaceholder.typicode.com")
conn.request("GET", "/posts/1")
response = conn.getresponse()
data = response.read()
json_data = json.loads(data)

print(json_data)