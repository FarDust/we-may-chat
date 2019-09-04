from django.urls import path, re_path
from django.conf.urls import url

from .views import new_message, get_data

urlpatterns = [
    path('new', new_message, name='records-new'),
    url(r'^getData/', get_data),
]