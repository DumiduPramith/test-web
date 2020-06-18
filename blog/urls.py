from django.urls import path
from .views import home, save_reply, create_question
# from .views import HomeListView

#your URLS

urlpatterns = [
    path('', home, name='blog-home'),
    path('<int:page_num>', home, name='blog-home'),
    path('reply/<int:key>', save_reply, name='reply-save'),
    path('question/new/', create_question, name='new-question'),
]
