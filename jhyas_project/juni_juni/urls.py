from django.urls import path
from .import views
from .views import PoetCreateView



urlpatterns = [
    path('', views.home, name = 'poet-home'),
    #path('', PostListView.as_view(), name = 'home'),
    path('poet/new/', PoetCreateView.as_view(), name = 'poet-create'),
    path('poet/<int:pk>/', views.poet_detail, name = 'poet-detail'),
    path('poet/register/', views.register, name='register'),
    path('poet/<int:pk>/delete/', views.delete, name='delete'),
    path('update/',views.update, name= 'update'),
]









