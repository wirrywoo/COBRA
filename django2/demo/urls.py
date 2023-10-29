from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('split-test/', TemplateView.as_view(template_name="index.html")),
] + staticfiles_urlpatterns()
