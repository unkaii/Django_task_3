from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload_view, name='upload'),
    path('file/<str:folder>/<str:filename>/', views.file_detail, name='file_detail'),

    # Новые маршруты для БД
    path('db/', views.db_list, name='db_list'),
    path('db/search/', views.db_search, name='db_search'),
    path('db/<int:pk>/edit/', views.db_edit, name='db_edit'),
    path('db/<int:pk>/delete/', views.db_delete, name='db_delete'),
]