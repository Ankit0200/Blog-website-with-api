from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.login_blog, name='login'),
    path(
        'register/', views.register_blog, name='register'
    ),
    path('logout/', views.logout_blog, name='logout'),

]