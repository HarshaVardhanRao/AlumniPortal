from django.urls import path
from portalapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.customLogin, name='login'),
    path('logout', views.customLogout, name='logout'),
    path('home',views.alumniHome, name='alumniHome'),
    path('events', views.alumniEvents, name='events'),
    path('successStrories', views.alumniSuccess, name='successStrories'),
    path('innovations', views.alumniInnovations, name='innovations'),
    path('createQuery', views.createQuery, name='createQuery'),
    path('aluminDashboard', views.alumniDashboard, name='aluminDashboard'),
    path('donations', views.donations, name='donations'),
]