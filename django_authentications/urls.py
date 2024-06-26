"""
URL configuration for django_authentications project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf import views
from drf_api_view import views as drf_api_view
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

router = DefaultRouter()
router.register('employee_api', drf_api_view.EmployeeViewSet, basename='employee')
urlpatterns = [

    path('social/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('todo/', include('todo.urls')),
    path('', include('blog.urls')),
    path('accounts/', include('accounts.urls')),
    path('drf/<int:pk>', views.student_detail),
    path('drf/', views.all_student),
    path('drfadd/', views.student_create),
    path("student_api", views.student_api),
    # path('employee_api',drf_api_view.List_create.as_view(),name="a"),
    # path('employee_api/<int:pk>',drf_api_view.retrieve_update_delete.as_view())
    path('apis/', include(router.urls)),
    path('api/gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
