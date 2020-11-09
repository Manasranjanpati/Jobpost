from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings

from .views import HomePage
from accounts.views import ApplicantSignUp, CompanySignUp, LoginView, UpdateApplicant, UpdateCompany


urlpatterns = [
    path('applicant/', include('applicantprofile.urls')),
    path('company/', include('companydashboard.urls')),
    path('jobs/', include('jobs.urls')),
    path('reg/company/<int:pk>/', UpdateCompany.as_view(extra_context={'title': 'Complete your Company\'s Profile'}), name='reg_company'),
    path('reg/profile/<int:pk>/', UpdateApplicant.as_view(extra_context={'title': 'Complete your Profile'}), name='reg_profile'),
    path('signup/company/', CompanySignUp.as_view(extra_context={'title': 'Employer SignUp'}), name='company_signup'),
    path('signup/applicant/', ApplicantSignUp.as_view(extra_context={'title': 'Applicant SignUp'}), name='applicant_signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='login'),
    path('', HomePage.as_view(), name='home'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)