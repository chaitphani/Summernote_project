from django.contrib import admin
from django.urls import path
from NJnaiduapp import views
from django.conf import settings
from django.conf.urls.static import static  

urlpatterns = [
    path('', views.index, name='index'),
    path('specialities/<slug:slug>/', views.specialities,name="spec"),
    path('category/<slug:slug>/', views.category,name="cate"),
    path('items/<slug:slug>/', views.items,name="items"),
    path('procedure/<slug:slug>/', views.procedure,name="procedure"),
    path('event', views.event,name='event'),
    path('our_team', views.our_team,name='our_team'),
   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)