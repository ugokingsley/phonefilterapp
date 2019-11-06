from django.db import models


class GsmFilter(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('date published', null=True)

    def __str__(self):
        return self.text

