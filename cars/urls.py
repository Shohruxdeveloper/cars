"""
URL configuration for cars project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path
from app.views import CarsAPIView, CarDetailAPIView, CarUpdateAPIView, CarDeleteAPIView, CarCreateAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/cars/", CarsAPIView.as_view()),
    path("api/cars/<int:pk>/", CarDetailAPIView.as_view()),
    path("api/cars/<int:pk>/update/", CarUpdateAPIView.as_view()),
    path("api/cars/<int:pk>/delete/", CarDeleteAPIView.as_view()),
    path("api/cars/<int:pk>/create/", CarCreateAPIView.as_view())

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)