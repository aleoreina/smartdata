from pickle import FALSE
from django.conf import settings
from core.models import PageProperties, Disclaimer

def disclaimer (request):

    try: 
        queryset = Disclaimer.objects.all()
    except :
        queryset = Disclaimer.objects.none()

    if queryset.count() > 0 :
        flag = True
    else :
        flag = False
    if flag == True :
        disclaimer  = {
            'disclaimer_title': queryset[0].title,
            'disclaimer_content': queryset[0].content,
            'disclaimer_status' : queryset[0].status         
        }
    else :
        disclaimer  = {
            'disclaimer_title': '',
            'disclaimer_content': '',
            'disclaimer_status' : False
        }

    return disclaimer

def pageproperties(request):
    slug = request.path 
    if request.path[:1] == "/" :
        slug = slug[1:]
    if request.path[-1:] == "/" :
        slug = slug[:-1]

    try: 
        queryset = PageProperties.objects.filter(slug=slug)
    except :
        quersyet = PageProperties.objects.none()

    if queryset.count() > 0 :
        flag = True
    else :
        flag = False

    if flag == True :
        pageproperties  = {
            'head_title' : queryset[0].head_title,
            'meta_description' : queryset[0].meta_description,
            'meta_keywords' : queryset[0].meta_keywords,
            'meta_robots' : queryset[0].meta_robots,
            'h1' : queryset[0].h1,
        }
    else :
        pageproperties  = {
            'head_title' : "Need to be created - head_title",
            'meta_description' : "Need to be updated - meta_description",
            'meta_keywords' : "Need to be updated - meta_keywords",
            'meta_robots' : "Need to be updated - meta_robots",
            'h1' : "Need to be updated - h1",
        }

    return pageproperties