from page.models import Page
from django.views.generic import DetailView
from money_internet_affiliate.models import AffiliatePage


class AffiliatePageView(DetailView):
    model = AffiliatePage
    template_name = "money_internet_affiliate/affiliate_page_view.html"
    obj_id = None

    def get_object(self, queryset=None):
        obj = super(AffiliatePageView, self).get_queryset()
        return obj.get(id=self.obj_id)    

