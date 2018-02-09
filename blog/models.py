from django.contrib.auth.models import User
from django.db import models


S_T_L = 4

class Article(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField()
	user = models.ForeignKey(User)
	release_date = models.DateField(null=True)

	def __str__(self):
		return self.title

	def get_short(self):
		if len(self.text) > S_T_L:
			return self.text[:S_T_L]
		else:
			return self.text