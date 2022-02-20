from importlib.metadata import distribution
from money_internet_affiliate.models.affiliate_models import InviteLink, InviteLinkHistory
from page.models import Page
from django.views.generic import DetailView
from money_internet_affiliate.models import AffiliatePage
import operator

class AffiliatePageView(DetailView):
    model = AffiliatePage
    template_name = "money_internet_affiliate/affiliate_page_view.html"
    obj_id = None

    def get_object(self, queryset=None):
        obj = super(AffiliatePageView, self).get_queryset()
        return obj.get(id=self.obj_id)    

class AffiliateRedirectPageView(DetailView):
    model = AffiliatePage
    template_name = "money_internet_affiliate/affiliate_redirect_page_view.html"
    obj_id = None

    def get_object(self, queryset=None):
        obj = super(AffiliateRedirectPageView, self).get_queryset()
        return obj.get(id=self.obj_id)    

    def get_context_data(self, **kwargs):
        context = super(AffiliateRedirectPageView, self).get_context_data(**kwargs)
        #LastInviteLink = InviteLinkHistory.objects.filter(site=self.get_queryset()).latest('created_at')
        '''
            InviteLinkHistory  
                .invitelink #InviteLinke
            InviteLink 
                .site #AffiliatePage
            
            AffiliatePage

            # [1,2,3]

            # Sacar los Links
            # Contabilizar hoy la distribucion por cada uno.
            # Sacar el numero menor,
            # Sacar el numero mayor
            # Comparar quien no tiene el numero mayor.
            # Si todos tienen el mismo numero, entonces el primer numero cargara se cedera.
            # Si no, Agarramos uno del numero menor y lo seleccionamos.

        '''
        AllLinks = InviteLink.objects.filter(site=self.get_queryset()[0])
        if AllLinks.count == 0 :
            return context

        #Hace redirect is AllLinks es 0.
        Distribution = {}
        import datetime
        today = datetime.date.today()

        for item in AllLinks:
            Distribution[item.pk] = InviteLinkHistory.objects.filter(invitelink=item, created_at__gt=today).count()



        id_min = min(Distribution.items(), key=operator.itemgetter(1))[0]

        print(Distribution)
        id_job = id_min
        InviteLinkJob = InviteLink.objects.get(id=id_job)
        HistoryCreate =InviteLinkHistory.objects.create(invitelink=InviteLinkJob)
        context['no_header'] = True
        context['no_footer'] = True

        context['invitelink'] = InviteLinkJob
        return context