
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('juni_juni.urls')),
    path('poet/login/',auth_views.LoginView.as_view(template_name='juni_juni/login.html'), name='login'),
    path('poet/logout/',auth_views.LogoutView.as_view(template_name='juni_juni/logout.html'), name='logout')
]

