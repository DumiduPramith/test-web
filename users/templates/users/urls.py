from django.urls import path
from .views import home, save_reply


urlpatterns = [
    path('', home, name='blog-home'),
    path('reply/<int:key>', save_reply, name='save-reply' )
]
