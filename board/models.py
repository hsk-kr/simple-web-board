from django.db import models


class Board(models.Model):
    title = models.TextField()
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
