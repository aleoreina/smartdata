from django.db.models.signals import pre_save
from django.dispatch import receiver
from core.tools.ip import IpTools
from core.middleware import RequestMiddleware

@receiver(pre_save)
def my_callback(sender, instance, *args, **kwargs):
    try:
        request = RequestMiddleware.thread_local
        if instance._state.adding:
            instance.created_ip = request.user_ip
            instance.created_country = request.user_ip_geolocation
    except:
        pass
