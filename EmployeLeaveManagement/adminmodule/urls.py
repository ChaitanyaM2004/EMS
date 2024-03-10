from django.urls import path
from .import views
urlpatterns = [
    path('', views.projecthomepage, name ='projecthomepage'),
    path('employhomepage', views.employhomepage, name ='employhomepage'),
    path('hrhomepage', views.hrhomepage, name ='hrhomepage'),
    path('signup', views.signup, name='signup'),
    path('signup1', views.signup1, name='signup1'),
    path('login', views.login, name='login'),
    path('login1', views.login1, name='login1'),
    path('logout', views.logout, name='logout'),
]
