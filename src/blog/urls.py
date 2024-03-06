from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='Home'),
    path('about/', views.about, name='About'),
    path('detail/<int:post_id>/', views.post_detail, name='detail'),
]