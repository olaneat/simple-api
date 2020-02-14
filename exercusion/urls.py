from django.urls import path
from .apiviews import ExecursionList

app_name = 'exercusion'
urlpatterns = [
    path('list', ExecursionList.as_view(), name='execursion_list'),
]
