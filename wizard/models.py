from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel, InlinePanel, StreamFieldPanel)
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail_app_pages.models import AppPageMixin
from wagtailtrans.models import TranslatablePage

from . import blocks


class FormWizardPage(AppPageMixin, TranslatablePage, Page):
    url_config = 'wizard.urls'

    content_panels = TranslatablePage.content_panels + [
        InlinePanel('forms')
    ]


class WizardForm(models.Model):
    page = ParentalKey(
        FormWizardPage, related_name='forms', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

    form_fields = StreamField([
        ('charfield', blocks.CharFieldBlock()),
    ])

    panels = [
        FieldPanel('title'),
        StreamFieldPanel('form_fields'),
    ]

    def __str__(self):
        return self.title
