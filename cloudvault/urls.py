"""
URL configuration for accounts project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('docs/', include_docs_urls(title='API Documentation')),
    path('accounts/', include('allauth.urls')),
    path('accounts/login/', include('allauth.urls')),
    path('accounts/logout/', include('allauth.urls')),
    path('accounts/inactive/', include('allauth.urls')),
    path('accounts/signup/', include('allauth.urls')),
    path('accounts/reauthenticate/', include('allauth.urls')),
    path('accounts/email/', include('allauth.urls')),
    path('accounts/accounts/confirm-email/', include('allauth.urls')),
    path('accounts/accounts/accounts/^confirm-email/', include('allauth.urls')),
    path('accounts/password/change/', include('allauth.urls')),
    path('accounts/password/set/', include('allauth.urls')),
    path('accounts/password/reset/', include('allauth.urls')),
    path('accounts/^password/reset/key/', include('allauth.urls')),
    path('accounts/password/reset/done/', include('allauth.urls')),
    path('accounts/login/code/confirm/', include('allauth.urls')),
    path('accounts/3rdparty/', include('allauth.urls')),
    path('accounts/social/login/cancelled/', include('allauth.urls')),
    path('accounts/social/login/error/', include('allauth.urls')),
    path('accounts/social/signup/', include('allauth.urls')),
    path('accounts/social/connections/', include('allauth.urls')),
]
