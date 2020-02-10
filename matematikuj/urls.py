from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.index, name="index"),
    path("studnice/", views.studnice, name="studnice"),
    path("priklady/", views.temata, name="temata"),
    path("priklady/<tema>/", views.podtemata, name="podtemata"),
    path("priklady/<tema>/<podtema>/", views.priklady, name="priklady"),
]
urlpatterns += staticfiles_urlpatterns()