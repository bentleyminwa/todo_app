from django.db import models
from django.contrib.auth.models import User


""" Main App model """
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)

    """ meta class  """
    class Meta:
        ordering = ["complete"]

    """ displays the title of the instance object """
    def __str__(self):
        return self.title 