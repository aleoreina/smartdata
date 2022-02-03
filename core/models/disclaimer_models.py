from django.db import models
from django.core.exceptions import ValidationError
from django.forms import BooleanField, CharField
from core.models import BaseModel


def validate_only_one_instance(obj):
    model = obj.__class__
    if (model.objects.count() > 0 and
            obj.id != model.objects.get().id):
        raise ValidationError("Can only create 1 %s instance" % model.__name__)


class Disclaimer (BaseModel):

    TYPE_CHOICES = [
    	("whole_site","For all Whole Site")
    ]   

    title = models.TextField()
    content = models.TextField()
    type = models.CharField(verbose_name="Type of Disclaimer", max_length=100,choices = TYPE_CHOICES ,default=TYPE_CHOICES[0][0])
    status = models.BooleanField()

    def __str__ (self):
        return str(self.pk) + " :: " + "Disclaimer of all Whole Site" 

    def clean(self):
        validate_only_one_instance(self)
