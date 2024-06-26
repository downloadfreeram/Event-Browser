from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("site/",views.site,name="site"),
    path("create/",views.create,name="create"),
    path("signout/", views.signout, name="signout"),
    path("eventslist/", views.eventslist, name="eventslist"),
    path("info/", views.info, name="info"),
    path("<int:id>",views.index, name="index"),
    path("mylist/",views.mylist,name="mylist"),
    path("deleteEvent/<int:id>",views.deleteEvent,name="deleteevent"),
    path("participate/<int:id>",views.participate, name="participate"),
    path("undoParticipate/<int:id>",views.undoParticipate, name="undoparticipate"),
    path("removeComment/<int:id>",views.removeComment, name="removecomment"),
]