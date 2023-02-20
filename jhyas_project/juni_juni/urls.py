from django.urls import path
from .import views
from .views import PoetCreateView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name = 'poet-home'),
    #path('', PostListView.as_view(), name = 'home'),
    path('poet/new/', PoetCreateView.as_view(), name = 'poet-create'),
    path('poet/<int:pk>/', views.poet_detail, name = 'poet-detail'),
    path('poet/register/', views.register, name='register'),
    path('poet/<int:pk>/delete/', views.delete, name='delete'),
    path('update/',views.update, name= 'update'),
]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)




