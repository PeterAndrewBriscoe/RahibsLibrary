from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="lib-home"),
    path('book/<int:id>/', views.show, name="book-show")
]

handler404 = 'lib.views.not_found_404'
handler500 = 'lib.views.server_error_500'