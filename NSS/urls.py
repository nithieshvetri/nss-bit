"""NSS URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.generic import RedirectView
from django.views.generic import TemplateView

from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from django.views.static import serve
handler404 = 'core.views.handler404' #'mysite.views.my_custom_page_not_found_view'
handler500 = 'core.views.handler500' 



urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root':settings.STATIC_ROOT}),
    # path('',RedirectView.as_view(url='admin/',permanent=False)),
    path('admin/', admin.site.urls),
            path('',TemplateView.as_view(template_name='index.html')),

    path('api/',include('core.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
