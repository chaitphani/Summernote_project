from django.contrib import admin
from django.apps import apps
from NJnaiduapp.models import *
# Register your models here.
from django.contrib.admin.sites import AlreadyRegistered
from django_summernote.admin import SummernoteModelAdmin

app_models = apps.get_app_config('NJnaiduapp').get_models()
for model in app_models:
    try:
        admin.site.register(model,SummernoteModelAdmin)
    except AlreadyRegistered:
        pass



# from django_summernote.admin import SummernoteModelAdmin

# class ItemAdmin(SummernoteModelAdmin):
#      summernote_fields = ('description')

# class SpecialitiesAdmin(SummernoteModelAdmin):
#      summernote_fields = ('speciality_description')

# class ProceduerAdmin(SummernoteModelAdmin):
#      summernote_fields = ('procedure_description')

