from django.db import models


class Board(models.Model):
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
