from django.db import models
from django.contrib.auth.models import User

class Reading(models.Model):
	day = models.IntegerField()
	verse = models.TextField()

	def __unicode__(self):
		return u'%s' % self.verse
# Create your models here.
