from django.urls import path, re_path
from apps.home import views
from apps.home.views import mark_visit
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # The home page
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

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
