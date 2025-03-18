
from django.contrib import admin
from django.urls import path
from .views import admin_login, admin_dashboard, admin_logout, delete_property, add_property, edit_property
from .views import admin_appointments, book_appointment, appointment_success
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', admin_login, name='admin_login'),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('logout/', admin_logout, name='admin_logout'),
    path('add-property/', add_property, name='add_property'),
    path('edit-property/<int:id>/', edit_property, name='edit_property'),
    path('delete-property/<int:id>/', delete_property, name='delete_property'),
    path('admin-appointments/', admin_appointments, name='admin_appointments'),
    path('book-appointment/', book_appointment, name='book_appointment'),
    path('appointment-success/', appointment_success, name='appointment_success'),

]
