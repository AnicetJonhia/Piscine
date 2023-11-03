# myapp/urls.py
from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('form_action/', views.form_action_view, name='form_action'),
]




