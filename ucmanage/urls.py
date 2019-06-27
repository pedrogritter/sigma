from django.conf import settings
from django.urls import include, path
from ucmanage import views as uc_views
from django.conf.urls.static import static

urlpatterns = [
    path('', uc_views.get_schedule, name='get_schedule'),

    path('list', uc_views.get_alunos_in_prof_uc, name='get_alunos_in_prof_uc')
    ]
