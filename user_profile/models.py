from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

class UserProfile(models.Model):
    
    user = models.OneToOneField(User)
    name = models.CharField(_("name"), max_length=50, null=True, blank=True)
    about = models.TextField(_("about"), null=True, blank=True)
    location = models.CharField(_("location"), max_length=40, null=True, blank=True)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='bookworm/originals/', blank=True, default='/media/default_user.jpg')
    genre_scores =  models.TextField(null=True, blank=True) # {"thriller":xxx,"drama":xxx,"mystery":xxx}
    likes = models.TextField(null=True, blank=True) # "[1,12,23]"
    #profile_skills = TaggableManager()
    def __unicode__(self):
        return self.user.username
