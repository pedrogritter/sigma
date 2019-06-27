from django.conf import settings
from django.conf.urls import url
from django.urls import include, path
from userprofiles import views as profile_views
from ucmanage import views as uc_views

from django.conf.urls.static import static


urlpatterns = [
    path('', profile_views.get_profile, name='get_profile'),
    path('details', profile_views.profile_details, name='profile_details'),
    path('schedule', uc_views.get_schedule, name='profile_schedule'),
    path('exams' , profile_views.profile_exams, name ='profile_exams'),
    path('results', profile_views.profile_results, name='profile_results'),
    path('change_password', profile_views.change_password, name='change_password'),
    path('edit_details', profile_views.edit_details, name='edit_details'),

]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
