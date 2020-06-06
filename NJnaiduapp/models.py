from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify

class User(models.Model):
    user_name = models.CharField(
        max_length=50, unique=True, null=True, blank=True)
    dateofbirth = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True,unique=True)
    mobile_number = models.CharField(max_length=15, null=True, blank=True)
    password = models.CharField(max_length=200, null=True, blank=True)
    address_line_1 = models.CharField(max_length=200, null=True, blank=True)
    address_line_2 = models.CharField(max_length=200, null=True, blank=True)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    remarks = models.CharField(max_length=200, null=True, blank=True)
    user_image = models.ImageField(upload_to='media', blank=True, null=True)
    active_from = models.DateTimeField(
        default=timezone.now, blank=True, null=True)
    active_to = models.DateTimeField(blank=True, null=True)
    last_login = models.DateTimeField(default=timezone.now, editable=False)
    last_ip_address=models.CharField(max_length=50,null=True,blank=True)

    # Relationship Fields
    created_user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='user_c_user',
                                     null=True, blank=True)
    modified_user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='user_m_user',
                                      null=True, blank=True)



    def __str__(self):
        return str(self.user_name)


class Item(models.Model):
    item_name = models.CharField(max_length=200,null=True,blank=True)
    slug = models.SlugField(max_length = 250, null = True, blank = True) 
    description=models.TextField(null=True,blank=True)
    item_image = models.ImageField(upload_to='itemimage', blank=True, null=True)
    meta_tag = models.CharField(max_length=30,null=True,blank=True)
    meta_title = models.CharField(max_length=200,null=True,blank=True)
    meta_description = models.CharField(max_length=200,null=True,blank=True)
    meta_keywords = models.CharField(max_length=200,null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    active_from = models.DateTimeField(
        default=timezone.now, blank=True, null=True)
    active_to = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=True)
    
    # Relationship Fields
    created_user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='item_c_user',
                                     null=True, blank=True)
    modified_user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='item_m_user',
                                      null=True, blank=True)

    
    def __str__(self):
        return str(self.item_name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.item_name)
        super(Item, self).save(*args, **kwargs)


class Category(models.Model):
    category_name = models.CharField(max_length=200,null=True,blank=True)
    slug = models.SlugField(max_length = 250, null = True, blank = True) 
    category_description=models.TextField(null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    active_from = models.DateTimeField(
        default=timezone.now, blank=True, null=True)
    active_to = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=True)
    
    # Relationship Fields
    item= models.ManyToManyField('Item',null=True,blank=True)
    created_user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='category_c_user',
                                     null=True, blank=True)
    modified_user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='category_m_user',
                                      null=True, blank=True)
    

    def __str__(self):
        return str(self.category_name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)


class Section1(models.Model):
    title = models.CharField(max_length=200,null=True,blank=True)
    description = models.TextField()
    section_image = models.ImageField(upload_to='section1', blank=True, null=True)
    mobile_number=models.CharField(max_length=15, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    active_from = models.DateTimeField(
        default=timezone.now, blank=True, null=True)
    active_to = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=True)
    
    # Relationship Fields
    created_user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='section1_c_user',
                                     null=True, blank=True)
    modified_user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='section1_m_user',
                                      null=True, blank=True)
    


    def __str__(self):
        return str(self.title)

class Section2(models.Model):
    title = models.CharField(max_length=200,null=True,blank=True)
    description =models.TextField()
    section2_image = models.ImageField(upload_to='section2', blank=True, null=True)
    section2background_image = models.ImageField(upload_to='section2back', blank=True, null=True)
    happy_patients=models.IntegerField(default='0',null=True,blank=True)
    surgeries=models.IntegerField(default='0',null=True,blank=True)
    doctors=models.IntegerField(default='0',null=True,blank=True)
    clinics=models.IntegerField(default='0',null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    active_from = models.DateTimeField(
        default=timezone.now, blank=True, null=True)
    active_to = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=True)
    
    # Relationship Fields
    created_user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='section2_c_user',
                                     null=True, blank=True)
    modified_user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='section2_m_user',
                                      null=True, blank=True)
    


    def __str__(self):
        return str(self.title)



class WhyUs(models.Model):
    title = models.CharField(max_length=200,null=True,blank=True)
    description =models.TextField()
    icon=models.CharField(max_length=200,null=True,blank=True)
    iconcolour=models.CharField(max_length=200,null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    active_from = models.DateTimeField(
        default=timezone.now, blank=True, null=True)
    active_to = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=True)
    
    # Relationship Fields
    created_user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='whyus_c_user',
                                     null=True, blank=True)
    modified_user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='whyus_m_user',
                                      null=True, blank=True)


    def __str__(self):
        return str(self.title)




class Procedure(models.Model):
    procedure_name = models.CharField(max_length=200,null=True,blank=True)
    procedure_description= models.TextField()
    slug = models.SlugField(max_length = 250, null = True, blank = True) 
    image = models.ImageField(upload_to='procedure', blank=True, null=True)
    meta_tag = models.CharField(max_length=30,null=True,blank=True)
    meta_title = models.CharField(max_length=200,null=True,blank=True)
    meta_description = models.CharField(max_length=200,null=True,blank=True)
    meta_keywords = models.CharField(max_length=200,null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    active_from = models.DateTimeField(
        default=timezone.now, blank=True, null=True)
    active_to = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=True)

    # Relationship Fields
    created_user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='procedure_c_user',
                                     null=True, blank=True)
    modified_user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='procedure_m_user',
                                      null=True, blank=True)
        


    def __str__(self):
        return str(self.procedure_name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.procedure_name)
        super(Procedure, self).save(*args, **kwargs)

class Specialities(models.Model):
    speciality_name = models.CharField(max_length=200,null=True,blank=True)
    speciality_description= models.TextField()
    slug = models.SlugField(max_length = 250, null = True, blank = True) 
    image = models.ImageField(upload_to='specialities', blank=True, null=True)
    meta_tag = models.CharField(max_length=30,null=True,blank=True)
    meta_title = models.CharField(max_length=200,null=True,blank=True)
    meta_description = models.CharField(max_length=200,null=True,blank=True)
    meta_keywords = models.CharField(max_length=200,null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    active_from = models.DateTimeField(
        default=timezone.now, blank=True, null=True)
    active_to = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=True)

    # Relationship Fields
    created_user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='specialities_c_user',
                                     null=True, blank=True)
    modified_user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='specialities_m_user',
                                      null=True, blank=True)
    Procedure = models.ManyToManyField('Procedure',blank=True, null=True)
        


    def __str__(self):
        return str(self.speciality_name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.speciality_name)
        super(Specialities, self).save(*args, **kwargs)

class Event(models.Model):
    event_name= models.CharField(max_length=200,null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    active_from = models.DateTimeField(
        default=timezone.now, blank=True, null=True)
    active_to = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=True)

    # Relationship Fields
    created_user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='event_c_user',
                                     null=True, blank=True)
    modified_user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='event_m_user',
                                      null=True, blank=True)
        


    def __str__(self):
        return str(self.event_name)





class ContactUsForm(models.Model):
    full_name= models.CharField(max_length=200,null=True,blank=True)
    email = models.EmailField(null=True, blank=True,unique=True)
    mobile_number = models.CharField(max_length=15, null=True, blank=True)
    subject= models.CharField(max_length=50,null=True,blank=True)
    message= models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    active_from = models.DateTimeField(
        default=timezone.now, blank=True, null=True)
    active_to = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=True)

    # Relationship Fields
    created_user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='contactusform_c_user',
                                     null=True, blank=True)
    modified_user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='contactusform_m_user',
                                      null=True, blank=True)
        


    def __str__(self):
        return str(self.full_name)


class Images(models.Model):
    image = models.ImageField(upload_to='images')
    name=models.CharField(max_length=50,null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    active_from = models.DateTimeField(
        default=timezone.now, blank=True, null=True)
    active_to = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=True)

    # Relationship Fields
    created_user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='images_c_user',
                                     null=True, blank=True)
    modified_user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='images_m_user',
                                      null=True, blank=True)
    events = models.ForeignKey('Event', on_delete=models.CASCADE,
                                     null=True, blank=True)
        


    def __str__(self):
        return str(self.name)



class Ourteam(models.Model):
    doctor_image = models.ImageField(upload_to='ourteam')
    doctor_name=models.CharField(max_length=50,null=True,blank=True)
    doctor_designation=models.CharField(max_length=50,null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    active_from = models.DateTimeField(
        default=timezone.now, blank=True, null=True)
    active_to = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=True)

    # Relationship Fields
    created_user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='ourteam_c_user',
                                     null=True, blank=True)
    modified_user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='ourteam_m_user',
                                      null=True, blank=True)
    specialities = models.ForeignKey('Specialities', on_delete=models.CASCADE,
                                     null=True, blank=True)


    def __str__(self):
        return str(self.doctor_name)