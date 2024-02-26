from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_user, name="login"),
    path("home/<str:name>", views.home, name="home"),
    path("question1/<str:name>", views.question1, name="question1"),
    path("question2/<str:name>", views.question2, name="question2"),
    path("question3/<str:name>", views.question3, name="question3"),
    path("question4/<str:name>", views.question4, name="question4"),
    path("complete/<str:name>", views.complete, name="complete"),
    path('logout/', views.logout_user, name='logout'),
]
