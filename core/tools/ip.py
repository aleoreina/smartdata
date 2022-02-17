class IpTools :
    def get_client_ip(request):
        try:
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        except:
            x_forwarded_for = None

        if x_forwarded_for != None:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        return ip