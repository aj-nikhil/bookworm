from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Author(models.Model):
	name = models.TextField(_("name"), null=False, blank=False)
	photo = models.ImageField(upload_to='bookworm/originals/', blank=True, default='/media/default_user.jpg')
	genre_scores =  models.TextField(null=True, blank=True) # {"thriller":xxx,"drama":xxx,"mystery":xxx}
	def __unicode__(self):
	        return self.name

class Book(models.Model):
	title = models.TextField(_("title"), null=False, blank=False)
	year = models.IntegerField(null=True, blank=True, default=0)
	country = models.CharField(_("country"), max_length=40, null=True, blank=True)
	photo = models.ImageField(upload_to='bookworm/originals/', blank=True, default='/media/default_user.jpg')
	author = models.ForeignKey(Author)
	download_link = models.URLField(blank=True)
	download_count = models.IntegerField(null=True, blank=True, default=0)
	genre_scores =  models.TextField(null=True, blank=True) # {"thriller":xxx,"drama":xxx,"mystery":xxx}

	def __unicode__(self):
	        return self.title

class Post(models.Model):    
	submiter = models.ForeignKey(User)
	title = models.TextField(_("title"), null=False, blank=False) 
	text = HTMLField()
	time_to_read = models.CharField(_("time_to_read"), max_length=50, null=True, blank=True)
	book = models.ForeignKey(Book)
	likes  = models.IntegerField(null=True, blank=True, default=0)
	published = models.DateTimeField(auto_now_add=True)
    
    	def __unicode__(self):
        	return self.title

class Comment(models.Model):
	submiter = models.ForeignKey(User)
	text = models.TextField(_("text"), null=False, blank=False)
	post = models.ForeignKey(Post)
