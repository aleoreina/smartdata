"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import include, path
from money_internet_affiliate.views import HomePageView
from money_internet_affiliate.views.homepage import AffiliatePageView
from money_internet_affiliate.views.homepage import TestView

urlpatterns = [
    path('', HomePageView.as_view(), name="homepage"),
    path('negocios-por-internet/columbustick', AffiliatePageView.as_view(), name="business-columbustick_profile"),
    path('test-step', TestView.as_view(), name="test-viewbusiness-columbustick_profile"),
]
