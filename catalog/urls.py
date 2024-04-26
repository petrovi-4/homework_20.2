from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.views import index, contact

app_name = 'catalog'

urlpatterns = [
    path('', index),
    path('contacts/', contact)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
