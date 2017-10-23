from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=50, null=True)
    body = models.TextField()
    author = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.title
