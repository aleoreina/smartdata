from django.urls import path
from django.contrib.contenttypes.models import ContentType


class URLSurrogate (object):

    @classmethod
    def generate_by_slug (self, **kwargs):
        
        view = kwargs.get('view_object')

        try:
            ct = ContentType.objects.get(
                app_label=kwargs.get('module_name'),
                model=kwargs.get('model_name')
                )
        except: 
            pass


        Model = ct.model_class()

        urlpatterns = []

        try: 
            try:
                objects = Model.objects.filter(status="published")
            except:
                objects = Model.objects.all()
        except:
            pass

        try: 
            for object in objects:
                urlpatterns += [path(object.slug, view.as_view(obj_id=object.id))]
        except: 
            pass

        return urlpatterns