from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from task1 import views

urlpatterns = [
    path('', views.main),
    path('second/', views.second_page),
    path('third/', views.third_page),
    path('registration/', views.sign_up_by_django),
    path('balance/', views.get_all)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)