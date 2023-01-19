from django.urls import path
from . import views



urlpatterns = [
    path('', views.notes, name='index'),
    path('categories/', views.categories, name='categories'),
    path('delete_document/<int:docid>/', views.delete_document, name='delete_document'),
    path('delete_category/<int:catid>/', views.delete_category, name='delete_category'),
    # path('sign_up/', views.sign_up, name='sign_up'),
    # path('show_category/', views.show_category, name='show_category'),
    # path('show_orders/', views.show_orders, name='show_orders'),

]
