from django.conf.urls import url

from .views import get_data

urlpatterns = [
    url(r'^getData/', get_data, name='data-source'),
]
