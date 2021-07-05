# name doesn't matter, but by convention

from django.urls import path
from . import views

# URLConf Module
#urlpatterns = [
#    path('playground/hello/', views.say_hello)
#]

# Every App can have its own URL Config

# But now we have to import into the main URL config for the project.

# Storefront URLS

# but now we don't need playground/, so now...


urlpatterns = [
    path('hello/', views.say_hello)
]
# Always end a route with a forward slash