from django.urls import path

from . import views
from .views import *


urlpatterns=[
    # path('help',views.help,name='HELP'),
    path('', views.survey_form_view, name='formpage'),
]