from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cobe-platform-demo/', TemplateView.as_view(template_name="index.html")),
    path('treatment-response/', views.clicked)
] + staticfiles_urlpatterns()
