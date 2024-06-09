from django.urls import path
from . import views

urlpatterns = [
    path('', views.start, name='start'),
    path('question/0/', views.question1, name='question1'),
    path('question/1/', views.question2, name='question2'),
    path('question/2/', views.question3, name='question3'),
    path('question/3/', views.question4, name='question4'),
    path('result/', views.result, name='result'),
]
