from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('Fondos.urls')),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
   # url(r'^',  RedirectView.as_view(url='inicio/login/')),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

