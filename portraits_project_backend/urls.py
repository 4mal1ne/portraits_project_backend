"""portraits_project_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# Django imports
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# DRF imports
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view


from main_app_ui.views import (
    home_page,
    about_artist,
    portfolio,
    price,
    testimonials,
)

API_TITLE = 'Artworks API'
API_DESCRIPTION = 'A work API for create, update and delete artworks and comments.'

schema_view = get_swagger_view(title=API_TITLE)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('portfolio/', portfolio),
    path('api/v1/create_auth/', include('rest_framework.urls')),  # Create registration.
    path('api/v1/artworks/', include('main_app.api.urls')),  # Anything after "api/" look for that path.
    path('docs/', include_docs_urls(
        title=API_TITLE,
        description=API_DESCRIPTION    # Add work API documentation from DRF.
    )
         ),
    path('swagger-docs/', schema_view),  # Add works API scheme.
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth_token/', include('djoser.urls.authtoken')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
