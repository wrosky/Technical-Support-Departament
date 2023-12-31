from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('create/', views.create_ticket, name = 'create_ticket'),
    path('list/', views.tickets_list, name = 'tickets_list'),
    path('register/', views.register_user, name = 'register'),
    path('login/', views.login_user, name = 'login'),
    path('logout/', views.logout_user, name = 'logout'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('customer_dashboard/', views.customer_dashboard, name = 'customer_dashboard'),
]