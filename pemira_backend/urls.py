"""
URL configuration for pemira_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from pemira_backend import settings
from pemira_backend.api.admin.admin import pemira_admin_site
from pemira_backend.api.auth.views.auth_view import AuthView
from pemira_backend.api.base.index_view import IndexView
from pemira_backend.api.candidate.views import CandidateView
from pemira_backend.api.vote.views import VoteView

router = SimpleRouter(trailing_slash=False)
router.register('auth', AuthView, basename='auth')
router.register('candidate', CandidateView, basename='candidate')
router.register('vote', VoteView, basename='vote')
urlpatterns = [
    path('', IndexView.as_view({'get': 'list'}), name='index'),
    path('admin/', pemira_admin_site.urls),
    path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
