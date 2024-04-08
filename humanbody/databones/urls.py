from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.tablesort, name='databones_home'),
    path('admin94/', admin.site.urls, name='dynamic_table_example' ),
    path('', include('django_dyn_dt.urls')),
    path('create', views.create, name='create'),
    path('<int:pk>', views.databones_Detailviev.as_view(), name='databones-detail'),
    path('<int:pk>/update', views.databones_Updateviev.as_view(), name='databones-update'),
    path('<int:pk>/delete', views.databones_Deleteviev.as_view(), name='databones-delete'),
    path('test', views.test_home, name='test'),
]