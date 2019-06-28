from django.conf import settings
from django.urls import include, path
from django.conf.urls import url
from userprofiles import views as profile_views
from django.conf.urls.static import static
from examemanage import views as exame_views

urlpatterns = [
    path('' , exame_views.get_exams, name='get_exams'),
    url(r'^exams/(?P<id>[\w-]+)/$', exame_views.inscrever, name='inscrever'),
]