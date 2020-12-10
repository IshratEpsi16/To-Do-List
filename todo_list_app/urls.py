from django.urls import path
from . import views
urlpatterns = [
    path('', views.lists),
    path('edit/<int:id>/', views.edit),
    path('delete/<int:id>', views.delete),



]
