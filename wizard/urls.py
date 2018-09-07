from django.urls import path

from .views import WizardView


urlpatterns = [
    path('', WizardView.as_view(), name='wizard'),
]
