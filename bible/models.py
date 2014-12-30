from django.db import models
from django.contrib.auth.models import User

class Reading(models.Model):
	day = models.IntegerField()
	verse = models.TextField()

	def __unicode__(self):
		return u'%s' % self.verse

class UserProfile(models.Model):
	user = models.ForeignKey(User, unique=True)
	day = models.IntegerField()
	startDate= models.DateField(auto_now_add = True)

	def __unicode__(self):
		return u'User: %s\tDay: %s' % (self.user, self.day)
