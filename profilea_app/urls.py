from django.urls import path, include
from .views import index_view


urlpatterns = [  
    path('accountant', index_view),
]