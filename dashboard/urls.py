from hashlib import new
from django.urls import path

from dashboard import views

urlpatterns = [
    path('',views.dashboard,name="Dashboard"),
    path('addbook/',views.addbook,name="Add Books"),
    path('opac/all/',views.showbook,name="OPAC"),
    path("bookadding/",views.addbooksub,name="BookAddedFormSubmit"),
    path('reports/',views.reports,name="Reports")
]