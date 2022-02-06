from pipes import Template
from django.shortcuts import render
from django.views.generic import TemplateView
from page.models import Page

class HomePageView(TemplateView):
    template_name = "homepage/homepage.html"

    def get_context_data(self, *args, **kwargs):

        context = super().get_context_data(*args, **kwargs)

        try :
            context['object'] = Page.objects.filter(slug="")[0]
        except :
            context['object'] = ""

        return context


class AffiliatePageView(TemplateView):
    template_name = "money_internet_affiliate/affiliate_page_view.html"

class TestView(TemplateView):
    template_name = "money_internet_affiliate/testview.html"

