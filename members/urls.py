from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_user, name="login"),
    path("home/<str:name>", views.home, name="home"),
    path("question1_luf/<str:name>", views.question1_luf, name="question1"),
    path("question2_gia/<str:name>", views.question2_gia, name="question2"),
    path("question3_bhe/<str:name>", views.question3_bhe, name="question3"),
    path("question4_nob/<str:name>", views.question4_nob, name="question4"),
    path("question5_zor/<str:name>", views.question5_zor, name="question5"),
    path("question6_kal/<str:name>", views.question6_kal, name="question6"),
    path("question7_sun/<str:name>", views.question7_sun, name="question7"),
    path("question8_nar/<str:name>", views.question8_nar, name="question8"),
    path("complete/<str:name>", views.complete, name="complete"),
    path('logout/', views.logout_user, name='logout'),
]
