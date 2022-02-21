from xml.etree.ElementInclude import include
from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('wallet', Wallet.as_view(), name='wallet')
]
