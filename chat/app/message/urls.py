from django.urls import path, re_path


from .views import new_message

urlpatterns = [
    path('new', new_message, name='records-new'),
]