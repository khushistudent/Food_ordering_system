from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name='home'),
    path('',views.home),
    path('about/',views.about,name='about'),
    path('menu/',views.menu,name='menu'),
    path('review/',views.review,name='review'),
    path('reservation/',views.reservation,name='reservation'),
    path('contact/',views.contact,name='contact'),
    path('login/',views.login,name='login'),
    path('register/',views.Register,name='Register'),
    
]