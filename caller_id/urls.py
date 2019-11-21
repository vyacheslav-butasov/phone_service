from django.urls import path
from . import views
from .apiviews import PhoneNumberList, PhoneNumberDetail


urlpatterns = [
    path('', views.index, name='index'),
    path('api/', PhoneNumberList.as_view()),
    path('api/<full_phone_number>/', PhoneNumberDetail.as_view())
]
