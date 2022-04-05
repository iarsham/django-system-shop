from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static


def home(request):
    return render(request, 'home.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    # Local Apps
    path('account/', include('account.urls')),
    path('store/', include('store.urls')),
    path('cart/', include('cart.urls')),
    path('order/', include('order.urls')),
    # 3rd Package
    path('__debug__/', include('debug_toolbar.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
