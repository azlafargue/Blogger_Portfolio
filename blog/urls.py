
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path # added include for debugger
import debug_toolbar 

from .views import index, blog, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('blog/', blog),
    path('about/', about),
]

if settings.DEBUG:
    urlpatterns += path('__debug__/', include(debug_toolbar.urls)),
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)