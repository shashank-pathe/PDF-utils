
from django.urls import path,include
from . import views
urlpatterns = [
        path('', views.home), 
        path("pdf", views.pdf_req)

              ]