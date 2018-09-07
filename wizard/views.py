from formtools.wizard.views import SessionWizardView


# temp
from django import forms
class Step1Form(forms.Form):
    foo = forms.CharField()
class Step2Form(forms.Form):
    bar = forms.CharField()
# /temp


class WizardView(SessionWizardView):
    form_list = [forms.Form]

    def get_form(self, step=None, data=None, files=None):
        form = super().get_form(step, data, files)
        import ipdb; ipdb.set_trace() 
