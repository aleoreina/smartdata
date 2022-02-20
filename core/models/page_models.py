from django.db import models
from core.models import AuditModel, SnippetCollection

class PageProperties(AuditModel):

	STATUS_CHOICES = [
	    ('unpublished',"Unpublished"),
		('scheduled',"Scheduled"),
	    ('published',"Published")
	]

	ROBOTS_CHOICES = [
		("index, follow","Index Page, Follow All Links"),
		("noindex, nofollow","No indexed, No follow links"),
		("noindex, follow","No indexed, Following Links"),
		("index, nofollow","Indexed, No Following Links"),
		("index","Just Indexed (Attention)"),
		("follow","Just Following Links (Attention)"),
		("noindex","No indexed (Attention)"),
		("nofollow","No followed links (Attention)"),
	]

	TYPE_CHOICES = [
		("dynamic","Dynamic"),
		("static","Static"),
	]
	
	h1 = models.CharField(max_length=200, unique=True, default='')
	head_title = models.CharField(verbose_name="Meta Title / Window Title", max_length=68, blank=False, null=False, unique=True)
	meta_description = models.CharField(verbose_name="Meta Description", max_length=155, blank=False, null=False, unique=True)
	meta_keywords = models.CharField(verbose_name="Meta Keywords", max_length=255, blank=False, null=False)
	meta_robots = models.CharField(verbose_name="Meta Robots", max_length=100,choices = ROBOTS_CHOICES ,default=ROBOTS_CHOICES[0][0])
	type = models.CharField(verbose_name="Type of page", max_length=100,choices = TYPE_CHOICES ,default=TYPE_CHOICES[0][0])
	slug = models.CharField(max_length=1000, unique=True, blank=True)
	status = models.CharField(choices=STATUS_CHOICES, default=STATUS_CHOICES[2][0], max_length=50)
	snippet_collection = models.ForeignKey(SnippetCollection, related_name='pageproperties_snippetcollection', on_delete=models.DO_NOTHING, blank=True)

	def __str__ (self):
		if self.slug == "" :
			slug = "Home Page"
		else :
			slug = self.slug

		return slug + " | " + self.h1