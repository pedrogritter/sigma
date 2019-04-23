from django.conf import settings
from django.urls import include, path
from userprofiles import views as profile_views
from django.conf.urls.static import static


urlpatterns = [
    path('', profile_views.get_profile, name='get_profile'),
    path('details', profile_views.profile_details, name='profile_details'),
    path('exams' , profile_views.profile_exams, name ='profile_exams')
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
