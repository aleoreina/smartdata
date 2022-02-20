import os, signal, sys
from django.conf import settings
from django.urls import clear_url_caches
from django.urls import path
from django.contrib.contenttypes.models import ContentType


class URLSurrogate (object):

    @classmethod
    def generate_by_slug (self, **kwargs):
        
        view = kwargs.get('view_object')
        prefix = kwargs.get('prefix') or None

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
                print(prefix)
                if prefix == None :
                    slug = object.slug
                else :
                    slug = prefix + "/" + object.slug
                urlpatterns += [path(slug, view.as_view(obj_id=object.id))]
        except: 
            pass

        return urlpatterns


# Reload URL Conf (Py3, DJ 3.1.17) - @aleoreina
def reload_urlconf(module=None, type_of_url="all", all_apps=False):

    def reload_module (module_name) :
        if module_name in sys.modules :
            print (module_name)
            reload(sys.modules[module_name])

    def get_all_urls_name (app_name) :
        _default = app_name + ".urls" 
        _admin = "_admin" 
        _admin = app_name + ".urls" + _admin
        _surrogate = "_surrogate" 
        _surrogate = app_name + ".urls"  + _surrogate

        if type_of_url == "all" :
            return [_default, _admin, _surrogate]
        elif type_of_url == "admin" : 
            return [_admin]
        elif type_of_url == "surrogate": 
            return [_surrogate]
        else :
            return [_default]

    to_process = [settings.ROOT_URLCONF]
    if all_apps == True :
        for module_in_app in settings.APP_MODULES :
            all_corresponding_individual_module = get_all_urls_name(module)           
            for item in all_corresponding_individual_module :
                to_process.append(item)
    else :
        all_corresponding_individual_module = get_all_urls_name(module)
        for item in all_corresponding_individual_module :
            to_process.append(item)

    def start() :
        def wsgi_fix():
            os.kill( os.getppid(), signal.SIGHUP )

        try: 
            wsgi_fix()
        except:
            pass    
        clear_url_caches()

        for collection_of_urls in to_process :
            reload_module(collection_of_urls)

        try: 
            wsgi_fix()
        except:
            pass    

    start()
    
    return True
    
    
    
    