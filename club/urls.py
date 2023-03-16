from django.urls import path
from django.urls import path
from .views import *

urlpatterns = [
    path('slider/', slider),
    path('get-media/', media),
    path('get-news/', news),
    path('get-forma/', forma),
    path('get-brand/', brand),
    path('get-statistica/', statistica),
    path('participant/', participant),
    path('opinion/', opinion),
    path('info-social/', info_social),
]