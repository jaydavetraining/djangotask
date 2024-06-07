from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    # path("january",views.jan),
    # path("february",views.feb),
    # path("challenges/<month>",views.monthsData),
    path("",views.index,name="index"),
    path("<int:month>",views.monthsDataNuber),
    path("<str:month>",views.monthsData,name="month-challenges")
    #  path("challenges/<int:month>",views.monthsDataNuber),
    # path("challenges/<str:month>",views.monthsData,name="month-challenges")
]

