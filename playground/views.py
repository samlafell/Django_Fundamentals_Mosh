from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> response
# request handler // action
# in django, it's called a 'view'
# but in Django, the normal 'view' is called a 'template'

def calculate():
    x = 1
    y = 2
    return x


def say_hello(request):
    x = calculate()
    # Pull data
    # Transform Data
    # Send Email
    # For now, response
  #return HttpResponse('Hello World')
    return render(request, 'hello.html', {'name' : 'Sam'})
    # Now need to map it to a View

# How can we use a template to return HTML content to the client?
# Add folder , 'templates', and add file