from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)  # title of the blog
    category = models.CharField(max_length=50, blank=True)  # tag of the blog
    date_time = models.DateField(auto_now_add=True)  # date of the blog
    content = models.TextField(blank=True, null=True)  # text

    def __unicode__(self):
        return self.title

    class Meta:  # descendant order by time
        ordering = ['-date_time']

