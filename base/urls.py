from django.urls import path
from . import views
from .views import view_ticket, delete_ticket, edit_ticket, change_ticket_status
from django.conf import settings
from django.conf.urls.static import static

# Ścieżki do widoków, dzięki nim możemy się poruszać po stronie
urlpatterns = [
    path('', views.home, name = 'home'),
    path('create/', views.create_ticket, name = 'create_ticket'),
    path('edit_ticket/<uuid:ticket_id>/', views.edit_ticket, name = 'edit_ticket'),
    path('delete_ticket/<uuid:ticket_id>/', views.delete_ticket, name = 'delete_ticket'),
    path('view_ticket/<uuid:uuid>/', view_ticket, name = 'view_ticket'),
    path('ticket/<uuid:ticket_id>/change_status/<str:new_status>/', change_ticket_status, name='change_ticket_status'),
    path('list/', views.tickets_list, name = 'tickets_list'),
    path('register/', views.register_user, name = 'register'),
    path('login/', views.login_user, name = 'login'),
    path('logout/', views.logout_user, name = 'logout'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('customer_dashboard/', views.customer_dashboard, name = 'customer_dashboard'),
    path('technik_dashboard/', views.technik_dashboard, name = 'technik_dashboard'),
]

# Warunki dla zczytytywania plików statycznych
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)