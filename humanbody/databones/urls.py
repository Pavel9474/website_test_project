from django.urls import path
from . import views

urlpatterns = [
    path('', views.databones_home, name='databones_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.databones_Detailviev.as_view(), name='databones-detail'),
    path('<int:pk>/update', views.databones_Updateviev.as_view(), name='databones-update'),
    path('<int:pk>/delete', views.databones_Deleteviev.as_view(), name='databones-delete')
]