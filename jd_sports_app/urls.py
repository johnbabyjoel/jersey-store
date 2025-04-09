from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name='jersey_list'),
    path('add/', views.add_jersey, name='add_jersey'),
    path('edit/<int:id>/', views.edit_jersey, name='edit_jersey'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

