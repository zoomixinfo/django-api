import requests

endpoint = "https://jsonplaceholder.typicode.com/posts"

get_response = requests.get(endpoint)

print(get_response.json())