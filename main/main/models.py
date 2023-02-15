from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from  django.core.validators import *
# Create your models here.
class Comments(models.Model):
  comment = models.TextField(max_length=350)
  at_game = models.IntegerField()
  stars = models.IntegerField( validators=[MinValueValidator(1), MaxValueValidator(100)])
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  date_created = models.DateTimeField(null=True, blank=True, default=timezone.now)