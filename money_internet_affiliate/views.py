from pipes import Template
from django.shortcuts import render
from django.views.generic import TemplateView

class AffiliateRedirectPageView(TemplateView):
    template_name = "money_internet_affiliate/affiliate_redirect_page.html"

class BaseSitePageView(TemplateView):
    template_name = "money_internet_affiliate/base_site.html"

