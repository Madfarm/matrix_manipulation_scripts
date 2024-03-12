import http.client

conn = http.client.HTTPSConnection("jsonplaceholder.typicode.com")
conn.request("GET", "/posts/1")
response = conn.getresponse()
data = response.read()

print(data)