from pipes import Template
from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "homepage/homepage.html"

class AffiliatePageView(TemplateView):
    template_name = "money_internet_affiliate/affiliate_page_view.html"

class TestView(TemplateView):
    template_name = "money_internet_affiliate/testview.html"

