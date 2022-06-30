from django.shortcuts import render
from django.views.generic import TemplateView
from page.models import Page


class LoginView(TemplateView):
    template_name = "core/login.html"

    def get_context_data(self, *args, **kwargs):

        context = super().get_context_data(*args, **kwargs)

        try:
            context['object'] = Page.objects.filter(slug="")[0]
        except:
            context['object'] = ""

        return context
