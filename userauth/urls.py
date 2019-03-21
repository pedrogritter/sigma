from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
import pages



urlpatterns = [
    path('', pages.views.landing, name="landing"),
    path('<slug:slug>/', views.authentication, name='authentication'),
    ]

    #path('accounts/signup/student/', views.SignUpView, name='student_signup'),
    #path('accounts/signup/teacher/', views.TeacherSignUpView, name='teacher_signup'),

    # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
