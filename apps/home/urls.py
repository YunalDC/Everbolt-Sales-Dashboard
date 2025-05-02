from django.urls import path, re_path, include
from apps.home import views
from apps.home.views import mark_visit
from django.conf import settings
from django.conf.urls.static import static
from .views import upload_customers

urlpatterns = [
    path('', views.index, name='home'),
    path("mark-visit/", mark_visit, name="mark_visit"),
    path('admin_panel.html', views.admin_panel, name='admin_panel'),
    path("map.html/", views.display_invoices, name="display_invoices"),
    path('upload-invoice/', views.upload_invoices, name='upload_invoice'),
    path('product-upload/', views.upload_products, name='product_upload'),
    path('notifications/', views.notifications_view, name='notifications'),
    path('assign-tasks/', views.assign_tasks_view, name='assign_tasks'),
    path('upload-collection/', views.upload_collection, name='upload_collection'),
    path('upload-product/', views.upload_products, name='upload_product'),
    path("products.html/", views.display_products, name="display_products"),
    path('collections/', views.view_collections, name='view_collections'),
    path('edit_users/', views.edit_users, name='edit_users'), 
    path('upload-customers/', upload_customers, name='upload_customers'),
    path('task/<int:task_id>/complete/', views.toggle_task_complete, name='toggle_task_complete'),
    path('task/<int:task_id>/delete/', views.delete_task, name='delete_task'),
    path("autocomplete-company/", views.autocomplete_company, name="autocomplete_company"),
]

# Serve media and static files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
    # Place catch-all only AFTER all specific routes
    urlpatterns += [re_path(r'^.*\.*', views.pages, name='pages')]
