from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.index, name="index"),
    path("studnice/", views.studnice, name="studnice"),
    path("priklady/", views.temata, name="temata"),
    path("priklady/<tema>/", views.podtemata, name="podtemata"),
    path("admin/pocet_uloh/", views.pocet_uloh, name="pocet_uloh"),
    path("priklady/<tema>/<podtema>/", views.priklady, name="priklady"),
]
urlpatterns += staticfiles_urlpatterns()