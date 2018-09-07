from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from .models import WizardForm


@modeladmin_register
class WizardFormAdmin(ModelAdmin):
    model = WizardForm
    menu_label = 'Wizard forms'
