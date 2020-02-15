from django.urls import path
from .apiviews import ExecursionList, ExecursionDetial

app_name = 'exercusion'
urlpatterns = [
    path('list', ExecursionList.as_view(), name='execursion_list'),
    path('detial/<int:pk>', ExecursionDetial.as_view(), name='execursion_detail'),
]

