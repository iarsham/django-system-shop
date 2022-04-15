from django.contrib import admin
from django.urls import path, include
from .handler import home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('account/', include('account.urls')),
    path('store/', include('store.urls')),
    path('cart/', include('cart.urls')),
    path('order/', include('order.urls')),

]

handler404 = 'config.handler.custom404'
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
