from django.urls import path
from .import views 
#app_name="home"
urlpatterns = [
path('',views.HomePageView.as_view(),name='home'),
path('about/',views.AboutPage.as_view(),name='about'),
]