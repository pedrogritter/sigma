from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

from pages import views as pages_views


urlpatterns = [
    #path('', include('pages.urls')),
    path('', views.signup, name='signup'),
    #path('accounts/', include('django.contrib.auth.urls')),
    #path('accounts/signup', views.SignUpView, name='signup'),
    #path('accounts/signup/student/', views.SignUpView, name='student_signup'),
    #path('accounts/signup/teacher/', views.TeacherSignUpView, name='teacher_signup'),
    ]
    # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
