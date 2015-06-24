from django.db import models

from datetime import datetime
from django.utils import timezone

from django.core.urlresolvers import reverse

# Create your models here.

class Task(models.Model):
    short_description = models.CharField(max_length=200)
    long_description = models.TextField()
    deadline = models.DateField()
    assigned_user = models.ForeignKey('account.MyUser', default=None, null=True)
    date_added = models.DateTimeField('date added', auto_now_add=True, null=True)
    last_modified = models.DateTimeField('last modified', auto_now=True, null=True)

    def __unicode__(self):
        return self.short_description

    def get_absolute_url(self):
        return reverse('taskmanager:edit', kwargs={"pk":self.id})

    class Meta:
        permissions = (
                ("create_task", "Can create new tasks"),
                ("edit_task", "Can modify tasks"),
                ("remove    _task", "Can delete tasks"),
        )