import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"  #"http://127.0.0.1:8000/" http://localhost:8000/

get_response = requests.post(endpoint,  json={'title': 'hello world', 'content': 'abc123', 'price': 'abc1234'}) #HTTP request
# print(get_response.text)#print raw text response
# print(get_response.status_code)


#HTTP REQUEST = HTML
#REST API HTTP REQUEST = JSON
#JAVASCRIPT OBJECT NOTATION = PYTHON DICTIONARY
print(get_response.json())
# print(get_response.status_code)