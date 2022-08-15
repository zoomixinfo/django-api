from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create your views here.
def index(request):
    #pull data from third party rest api
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    #convert reponse data into json
    users = response.json()
    #print(users)
    return render(request, "index.html",{'users': users})
    pass