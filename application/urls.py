from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # path('show_category/', views.show_category, name='show_category'),
    # path('show_orders/', views.show_orders, name='show_orders'),

]
