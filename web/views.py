from django.shortcuts import render
from django.http import HttpResponse # para dar una respuesta en la página, lo que va a pintar en la página
from django.contrib.auth.models import User
import random
from .models import Name

from rest_framework import viewsets
from rest_framework import permissions
from web.serializers import NameSerializer, UserSerializer
from web.models import Name
from rest_framework import generics

# siempre como input request, que son las peticiones que nos van a llegar
# para que esto sepa donde devolver tenemos que crear urls.py de la app y de la web
def index(request) :
    r = random.randint(0,10)
    print(type(Name.objects))
    names_with_a = Name.objects.order_by('text')[:5]
    print(names_with_a)
    output = ', '.join(n.text for n in names_with_a)

    return HttpResponse("Hello BRIDGERS! : <b>{0}</b>".format(output))

# para que esto sepa donde devolver tenemos que crear urls.py de la app y de la web

def xxxx(request) :
    return HttpResponse("xxxx")

class NameViewSet(viewsets.ModelViewSet):
    print("YEAH!")
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Name.objects.all()
    serializer_class = NameSerializer
    lookup_field = 'text'
#    permission_classes = [permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    print("YEAH!")
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]