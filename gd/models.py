from django.db import models
from wagtail.core.models import Page
from wagtail_app_pages.models import AppPageMixin
from wagtailtrans.models import TranslatablePage


class GDPage(AppPageMixin, TranslatablePage, Page):
    url_config = 'gd.urls'


class Hobby(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Hobbies'


class Job(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    hobbies = models.ManyToManyField(Hobby)
    job = models.ForeignKey(
        Job, related_name='people', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        verbose_name_plural = 'People'
