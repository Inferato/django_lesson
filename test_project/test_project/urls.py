"""
URL configuration for test_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from blogpost.views import PostsList

schema_view = get_schema_view(
   openapi.Info(
      title="BlogPost Docker API",
      default_version='v1',
      description="Here is a simple DRF",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('polls.urls')),
    path('', include('logistration.urls')),
    path('api/', include('blogpost.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),
    path('post-list/', PostsList.as_view(), name='post_list'),
    path('blog/', include('blog.urls'))
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += [path('i18n/', include('django.conf.urls.i18n'))]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
