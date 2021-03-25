from django.db import models


class Entry(models.Model):
    url = models.URLField(max_length=300)
    status_code = models.CharField(max_length=10)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url
