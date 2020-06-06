from django.contrib import admin
from django.urls import path
from adminapp import views
from django.conf import settings
from django.conf.urls.static import static  

urlpatterns = [
    path('', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),


    ###########  Signup  ###############

    path('signup_create', views.signup_create, name='signup_create'),
    path('signup_list', views.signup_list, name='signup_list'),
    path('signup_edit/<int:pk>', views.signup_edit, name='signup_edit'),
    path('signup_delete/<int:pk>', views.signup_delete, name='signup_delete'),

    ########## LOGIN #################

    path('logout', views.logout, name='logout'),
    path('forget_password', views.forget_password, name='forget_password'),
    path('otp', views.otp, name='otp'),
    path('set_password', views.set_password, name='set_password'),

    ###############  ITEM ##########

    path('item_create', views.item_create, name='item_create'),
    path('item_list', views.item_list, name='item_list'),
    path('item_view/<int:pk>', views.item_view, name='item_view'),
    path('item_edit/<int:pk>', views.item_edit, name='item_edit'),
    path('item_delete/<int:pk>', views.item_delete, name='item_delete'),
    path('contact', views.contact, name = 'contact'),


    ###############  Category ##########

    path('category_create', views.category_create, name='category_create'),
    path('category_view/<int:pk>', views.category_view, name='category_view'),
    path('category_list', views.category_list, name='category_list'),
    path('category_edit/<int:pk>', views.category_edit, name='category_edit'),
    path('category_delete/<int:pk>', views.category_delete, name='category_delete'),


    ###############  Section1 ##########

    path('sec1_create', views.sec1_create, name='sec1_create'),
    path('sec1_view/<int:pk>', views.sec1_view, name='sec1_view'),
    path('sec1_list', views.sec1_list, name='sec1_list'),
    path('sec1_edit/<int:pk>', views.sec1_edit, name='sec1_edit'),
    path('sec1_delete/<int:pk>', views.sec1_delete, name='sec1_delete'),

    ###############  Section2 ##########

    path('sec2_create', views.sec2_create, name='sec2_create'),
    path('sec2_view/<int:pk>', views.sec2_view, name='sec2_view'),
    path('sec2_list', views.sec2_list, name='sec2_list'),
    path('sec2_edit/<int:pk>', views.sec2_edit, name='sec2_edit'),
    path('sec2_delete/<int:pk>', views.sec2_delete, name='sec2_delete'),
   

   
    ###############   Why Us ##########

    path('whyus_create', views.whyus_create, name='whyus_create'),
    path('whyus_view/<int:pk>', views.whyus_view, name='whyus_view'),
    path('whyus_list', views.whyus_list, name='whyus_list'),
    path('whyus_edit/<int:pk>', views.whyus_edit, name='whyus_edit'),
    path('whyus_delete/<int:pk>', views.whyus_delete, name='whyus_delete'),

     ###############  Our TEAM ##########

    path('ourteam_create', views.ourteam_create, name='ourteam_create'),
    path('ourteam_view/<int:pk>', views.ourteam_view, name='ourteam_view'),
    path('ourteam_list', views.ourteam_list, name='ourteam_list'),
    path('ourteam_edit/<int:pk>', views.ourteam_edit, name='ourteam_edit'),
    path('ourteam_delete/<int:pk>', views.ourteam_delete, name='ourteam_delete'),

     ###############  Specialities ##########

    path('specialities_create', views.specialities_create, name='specialities_create'),
    path('specialities_view/<int:pk>', views.specialities_view, name='specialities_view'),
    path('specialities_list', views.specialities_list, name='specialities_list'),
    path('specialities_edit/<int:pk>', views.specialities_edit, name='specialities_edit'),
    path('specialities_delete/<int:pk>', views.specialities_delete, name='specialities_delete'),

     ###############  Procedure ##########

    path('procedure_create', views.procedure_create, name='procedure_create'),
    path('procedure_view/<int:pk>', views.procedure_view, name='procedure_view'),
    path('procedure_list', views.procedure_list, name='procedure_list'),
    path('procedure_edit/<int:pk>', views.procedure_edit, name='procedure_edit'),
    path('procedure_delete/<int:pk>', views.procedure_delete, name='procedure_delete'),

     ###############  Event ##########

    path('event_create', views.event_create, name='event_create'),
    path('event_view/<int:pk>', views.event_view, name='event_view'),
    path('event_list', views.event_list, name='event_list'),
    path('event_edit/<int:pk>', views.event_edit, name='event_edit'),
    path('event_delete/<int:pk>', views.event_delete, name='event_delete'),

     ###############  Images ##########

    path('image_create', views.image_create, name='image_create'),
    path('image_view/<int:pk>', views.image_view, name='image_view'),
    path('image_list', views.image_list, name='image_list'),
    path('image_edit/<int:pk>', views.image_edit, name='image_edit'),
    path('image_delete/<int:pk>', views.image_delete, name='image_delete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)