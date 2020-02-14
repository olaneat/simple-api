from django.urls import path
from .apiviews import UserReg

app_name = 'account'

urlpatterns = [
    path('signup', UserReg.as_view(), 'signup'),
]
