from django.db import models


class Group(models.Model):
    title = models.CharField(max_length=64, unique=True, null=True, blank=False)


class User(models.Model):
    name = models.CharField(max_length=64, unique=True, blank=False)
    first_name = models.CharField(max_length=64, null=True)
    last_name = models.CharField(max_length=64, null=True)
    age = models.PositiveIntegerField()
    group = models.ForeignKey(Group, related_name='users', on_delete=models.CASCADE)
