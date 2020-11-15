
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from posts.views import posts


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls', namespace='auth')),
    path('posts/', include('posts.urls', namespace='post')),
    path('', posts),
    path('api/', include('authentication.api.urls')),
    path('api-auth/', include('rest_framework.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
