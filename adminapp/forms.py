from NJnaiduapp.models import  *

from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django import forms
from django.forms import ModelForm
from django.forms import ImageField as DjangoImageField 

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        exclude=('login_required','created_date','modified_date','active_from','active_to','last_login','last_ip_address','created_user','modified_user','remarks','status')



class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category    
        fields = ('category_name','category_description','status','item')
        widgets = {
            'category_description': SummernoteWidget(attrs={'summernote':{'width':'100%'}}),
            # 'bar': SummernoteInplaceWidget(),
        }
        

class Sec1Form(forms.ModelForm):
    class Meta:
        model = Section1    
        fields = ('title','description','section_image','mobile_number','status')
        

class Sec2Form(forms.ModelForm):
    class Meta:
        model = Section2    
        fields = ('title','description','section2_image','section2background_image','happy_patients','surgeries','doctors','clinics','status')
      
class WhyUsForm(forms.ModelForm):
    class Meta:
        model = WhyUs    
        fields = ('title','description','icon','status')

      
class OurteamForm(forms.ModelForm):
    class Meta:
        model = Ourteam    
        fields = ('doctor_image','doctor_name','doctor_designation','specialities','status')

      
class EventForm(forms.ModelForm):
    class Meta:
        model = Event    
        fields = ('event_name','status',)

      
class ImageForm(forms.ModelForm):
    class Meta:
        model = Images    
        fields = ('image','name','events',)
      
      

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('description','item_name','item_image')
        widgets = {
            'description': SummernoteWidget(attrs={'summernote':{'width':'100%'}}),
            # 'bar': SummernoteInplaceWidget(),
        }
    # def __init__(self,  *args, **kwargs):
    #     super(ItemForm, self).__init__(*args, **kwargs)
    #     self.fields['description'] =forms.CharField(widget=SummernoteWidget(attrs={'summernote': {'width': '50%', 'height': '400px'}}))


class SpecialitiesForm(forms.ModelForm):
    class Meta:
        model = Specialities
        fields = ('speciality_name','speciality_description','meta_tag','meta_title','meta_description','meta_keywords','Procedure','status')
        widgets = {
           'speciality_description': SummernoteWidget(attrs={'summernote':{'width':'100%'}}),
            # 'bar': SummernoteInplaceWidget(),
        }
    # def __init__(self, *args, **kwargs):
    #     super(SpecialitiesForm, self).__init__(*args, **kwargs)
    #     self.fields['speciality_description'] =forms.CharField(widget=SummernoteWidget(attrs={'summernote': {'width': '50%', 'height': '400px'}}))


class ProceduerForm(forms.ModelForm):
    class Meta:
        model = Procedure
        fields = ('procedure_name','procedure_description','status')
        widgets = {
           'procedure_description': SummernoteWidget(attrs={'summernote':{'width':'100%'}}),
            # 'bar': SummernoteInplaceWidget(),
        }  
    # def __init__(self, *args, **kwargs):
    #     super(ProceduerForm, self).__init__(*args, **kwargs)
    #     self.fields['procedure_description'] =forms.CharField(widget=SummernoteWidget(attrs={'summernote': {'width': '50%', 'height': '400px'}}))



# class SuccessStoriesForm(forms.ModelForm):
#     class Meta:
#         model = Item
#         fields = ('description','item_name','item_url','item_image')
#         widgets = {
#             'foo': SummernoteWidget(),
#             'bar': SummernoteInplaceWidget(),
#         }
#     def __init__(self, ticket, *args, **kwargs):
#         super(ItemForm, self).__init__(*args, **kwargs)
#         self.fields['description'] =forms.CharField(widget=SummernoteWidget(attrs={'summernote': {'width': '50%', 'height': '400px'}}))