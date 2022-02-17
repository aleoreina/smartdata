import threading
from .tools import IpTools
from django.contrib.gis.geoip2 import GeoIP2

class RequestMiddleware(object):
    thread_local = threading.local()
    
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        # Almacenamos en el usuario que esta en el request
        self.thread_local.user = request.user
        self.thread_local.user_ip = IpTools.get_client_ip(request)
        if self.thread_local.user_ip == "127.0.0.1" :
            self.thread_local.user_ip_geolocation = "localhost"
        else :
            g = GeoIP2()
            try:
                self.thread_local.user_ip_geolocation = g.country(self.thread_local.user_ip)['country_name']
            except:
                self.thread_local.user_ip_geolocation = "localhost"
                
        response = self.get_response(request)
        return response
