from django.db import models
from .forms import User


class Input(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    input_values = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
