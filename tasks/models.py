from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    deadline_date = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tag_ids = models.ManyToManyField(
        Tag,
        related_name='tasks',
        blank=True,
        null=True,
    )
