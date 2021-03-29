from django.db import models


# class EntryManager(models.Manager):
#     def get_queryset(self):
#         return super(EntryManager, self).get_queryset().order_by('-timestamp')


class Entry(models.Model):
    url = models.URLField(max_length=300)
    status_code = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    # objects = EntryManager()

    def __str__(self):
        return self.url
