from django.db import models
from django.utils.text import slugify


class Blog(models.Model):
    title = models.CharField(max_length=50, null=True)
    body = models.TextField()
    author = models.CharField(max_length=50, null=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.title + '-' + self.author
    
    def get_absolute_url(self):
        return "/%s" % self.slug

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(Blog, self).save(*args, **kwargs)

    def author_slug(self):
        return "Publisher: %s - %s" % (self.author, self.slug)