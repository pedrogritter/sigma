from django.conf import settings
from django.urls import include, path
from presences import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.PresencaListView, name='register_presenca'),
    path('list/', views.get_presencas, name='list_presenca')
    ]
