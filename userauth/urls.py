from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

import pages



urlpatterns = [
    path('', pages.views.landing, name="landing"),
    # path('^signup/&', views.signup, name='signup'),
    # path('^login', views.login, name='login'),
    # path('^logout', views.logout, name='logout'),
    path('<slug:slug>/', views.authentication, name='authentication'),
    ]
    #url('^login', views.login, name='login'),
    #url('^logout', views.logout, name='logout'),
    #path('accounts/', include('django.contrib.auth.urls')),
    #path('accounts/signup', views.SignUpView, name='signup'),
    #path('accounts/signup/student/', views.SignUpView, name='student_signup'),
    #path('accounts/signup/teacher/', views.TeacherSignUpView, name='teacher_signup'),

    # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
