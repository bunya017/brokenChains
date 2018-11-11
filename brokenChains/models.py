from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
	if created:
		Token.objects.create(user=instance)


class Habit(models.Model):
	name = models.CharField(max_length=50)
	owner = models.ForeignKey(User, related_name='habits', on_delete=models.CASCADE)
	goal = models.CharField(max_length=150)
	start_date = models.DateField(auto_now_add=True)
	stop_date = models.DateField(blank=True, null=True)

	class Meta:
		ordering = ('start_date',)
		unique_together = ('owner', 'name')

	def save(self, *args, **kwargs):
		self.name = self.name.title()
		self.goal = self.goal.title()
		super(Habit, self).save(*args, **kwargs)

	def __str__(self):
		return self.name.title()


class Session(models.Model):
	habit = models.ForeignKey(Habit, related_name='sessions', on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	text = models.CharField(max_length=200, blank=True) # For additional notes
	date = models.DateField(auto_now_add=True)
	is_complete = models.BooleanField(default=False)

	class Meta:
		ordering = ('date',)
		unique_together = ('habit', 'name')

	def save(self, *args, **kwargs):
		if self.habit.name in self.name:
			self.name = self.name.title()
			pass
		else:
			self.name = self.habit.name +" - "+ self.name.title()
		super(Session, self).save(*args, **kwargs)

	def __str__(self):
		return self.name.title()
	