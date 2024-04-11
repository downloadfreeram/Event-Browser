from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("site/",views.site,name="site"),
    path("create/",views.create,name="create"),
    path("signout/", views.signout, name="signout"),
]