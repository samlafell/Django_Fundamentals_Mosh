from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> response
# request handler // action
# in django, it's called a 'view'
# but in Django, the normal 'view' is called a 'template'

#def say_hello(request):
    # Pull data
    # Transform Data
    # Send Email
    # For now, response
 #   return HttpResponse('Hello World')
    # Now need to map it to a View

# How can we use a template to return HTML content to the client?
# Add folder , 'templates', and add file

# Render a template and return HTML markup
def say_hello(request):
    return render(request, 'hello.html')