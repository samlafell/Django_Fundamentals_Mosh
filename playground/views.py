from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> response
# request handler // action
# in django, it's called a 'view'
# but in Django, the normal 'view' is called a 'template'

def say_hello(request):
    # Pull data
    # Transform Data
    # Send Email
    # For now, response
    return HttpResponse('Hello World')
    # Now need to map it to a View