from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class PageProperties(models.Model):

	ROBOTS_CHOICES = [
		("index, follow","All"),
		("noindex, nofollow","None"),
		("noindex, follow","No index, Follow"),
		("index, nofollow","Index, No follow"),
		("index","Index"),
		("follow","Follow"),
		("noindex","No index"),
		("nofollow","No follow"),
	]

	#content_type = models.ForeignKey(ContentType, related_name="content_type_timelines", null=True, on_delete=models.SET_NULL)
	#object_id = models.PositiveIntegerField()
	#content_object = GenericForeignKey('content_type', 'object_id')
	head_title = models.CharField(verbose_name="Meta Title / Window Title", max_length=68, blank=False, null=False, unique=True)
	meta_description = models.CharField(verbose_name="Meta Description", max_length=155, blank=False, null=False, unique=True)
	meta_keywords = models.CharField(verbose_name="Meta Keywords", max_length=255, blank=False, null=False)
	#featured_image = models.ImageField(upload_to = upload_image_page_properties, default = 'service/no-img.png')
	meta_robots = models.CharField(verbose_name="Meta Robots", max_length=100,choices = ROBOTS_CHOICES ,default=ROBOTS_CHOICES[0][0])
	slug = models.CharField(max_length=1000, unique=True)
