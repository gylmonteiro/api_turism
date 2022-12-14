"""api_turism URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from turistics_points.views import TuristicPointView
from equipments.views import EquipmentView
from assessments.views import AssessmentView
from comments.views import CommentView
from localizations.views import LocalizationView
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'pontosturisticos',TuristicPointView, basename = "TuristicPoint")
router.register(r'equipamentos', EquipmentView)
router.register(r'avaliacoes', AssessmentView)
router.register(r'comentarios', CommentView)
router.register(r'localizacoes', LocalizationView)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("login/", (obtain_auth_token)),
]
