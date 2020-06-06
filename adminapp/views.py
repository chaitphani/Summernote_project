from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from NJnaiduapp.models import *
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password
# from myproject.utils import is_authenticated
from random import randint
from django.core.mail import send_mail
from  NJnaiduportal import settings
import socket
from django.db.models import Q
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from NJnaiduapp.forms import *
from adminapp.forms import *
from django.utils.timezone import datetime 
from NJnaiduportal.utils import is_authenticated
from datetime import datetime


################### SIGNUP CREATE #######################
@is_authenticated
def signup_create(request):
    form = SignupForm(request.POST,request.FILES)    
    if request.method == "POST":
        email=request.POST['email']
        username=request.POST['user_name']
        mobile=request.POST['mobile_number']
        try:
            user=User.objects.filter(Q(email=email)|Q(mobile_number=mobile)|Q(user_name=username))
            if user:
                messages.error(request,'email or mobile or username already exist')
                return redirect('signup_create')
        except:
            pass
    if request.method == "POST":
        if form.is_valid():
            post=form.save(commit=False)
            post.password=make_password(request.POST['password'])
            post.save()
            subject="USER credentials"
            message="user logged in details are"+request.POST['password']+request.POST['email']+request.POST['user_name']
            message_title="USER Credentials" 
            send_mail(email,subject,message,message_title=None)
            return redirect('signup_list')
    return render(request,'User/signup-create.html',{'form':form})
    
@is_authenticated      
def signup_list(request):
    form =User.objects.all()
    return render(request,'User/signup-list.html',{'form':form})

@is_authenticated
def user_view(request, pk):
    book= get_object_or_404(User, pk=pk)    
    return render(request, 'User/user-detail.html', {'loki':book})

@is_authenticated
def signup_edit(request,pk):
    book=get_object_or_404(User,pk=pk)    
    if request.method == "POST":
        form=SignupForm(request.POST,request.FILES,instance=book)        
        if form.is_valid():
            post=form.save(commit=False)
            post.password=make_password(request.POST['password'])
            post.save()
            return redirect('signup_list')
    else:
        form=SignupForm(instance=book)        
        return render(request,'User/signup-create.html',{'form':form,'book':book})

@is_authenticated
def signup_delete(request,pk):
    form=User.objects.get(pk=pk)
    form.delete()
    return redirect('signup_list')


############### USER LOGIN   ######################

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.get(email=email)
        except:
            user = False
            messages.error(request, 'Invalid Email')
            return redirect('login')
        match = check_password(password, user.password)
        if match:
            print("success")
            request.session['pk']=user.id 
            request.session['mobile']=user.mobile_number
            hostname = socket.gethostname()    
            IPAddr = socket.gethostbyname(hostname) 
            user.last_ip_address = IPAddr
            user.last_login = datetime.today()
            user.save()
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Password')
            return redirect('login')
    return render(request, 'User/login.html', {})

def dashboard(request):
    return render(request,'User/index.html',{})

def logout(request):
    del request.session['pk']
    del request.session['mobile']
    return render(request,'User/login.html',{})

def forget_password(request):
    if request.method == 'POST':
        email=request.POST['email']
        try:
            userr=User.objects.get(email=email)
        except:
            userr=False
        if userr:
            request.session['pk']=userr.id
            otp=randint(4000,10000)
            print(otp)
            request.session['otp']=otp  
            subject="Forgot PAssword"
            message = "We received a for got password request from your account.\nMake sure not to share your OTP with anyone.\n OTP :{}.\n\n\nplease verify your account if it's not you".format(
                str(otp))
            from_email = settings.EMAIL_HOST_USER
            send_mail(subject, message, from_email, [
                email], fail_silently=False)         
            return redirect('otp')
        else:
            print('enter valid email')
            messages.error(request,'enter valid email')
            return redirect('forget_password')
    return render(request,'User/forget-password.html')


def otp(request):
    if request.method == 'POST':
        otp=request.POST['otp']
        if int(request.session['otp']) == int(otp):
            return redirect('set_password')
        else:
            print('enter valid otp')
            message="enter valid otp"
            messages.error(request,message)
            return redirect('otp')
    else:
        return render(request,'User/otp.html')

def set_password(request):
    loguser=User.objects.get(id=request.session['pk'])
    if request.method == 'POST':
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        if str(password)==str(confirm_password):
            loguser.password=make_password(password)
            loguser.save()
            return redirect('login')
        else:
            message="enter valid "            
            messages.error(request,messages)
            return redirect('otp')
    else:
        return render(request,'User/set-password.html')




#####################  ITEM VIEW #############################

@is_authenticated
def item_create(request):
    user=User.objects.get(id=request.session['pk'])
    form = WhyUsForm(request.POST,request.FILES)
    if request.method == "POST":
        sec = request.POST.get('on')       
        if form.is_valid():
            section=form.save(commit=False)
            section.created_user=user
            section.created_date= datetime.today()
            if sec == 'on':
                section.status=True
                section.save()
            else:
                section.status=False
                section.save()
            return redirect('item_list')
    return render(request, 'Item/item-create.html', {'form':form})

@is_authenticated
def item_view(request, pk):
    book= get_object_or_404(Item, pk=pk)    
    return render(request, 'Item/item-detail.html', {'loki':book})

@is_authenticated
def item_list(request):
    form =Item.objects.all()
    return render(request,'Item/item-list.html',{'form':form})

@is_authenticated
def item_edit(request,pk):
    book = Item.objects.first()
    user=User.objects.get(id=request.session['pk'])
    form=ItemForm(instance=book)    
    if request.method == "POST":
        sec = request.POST.get('on')       
        form=ItemForm(request.POST,request.FILES,instance=book)       
        if form.is_valid():
            section=form.save(commit=False)
            section.modified_user=user
            section.modified_date=datetime.today()
            if sec == 'on':
                section.status=True
                section.save()
            else:
                section.status=False
                section.save()
            return redirect('item_list')    
    return render(request,'Item/item-create.html',{'form':form,'book':book})

@is_authenticated
def item_delete(request,pk):
    form=Item.objects.get(pk=pk)
    form.delete()
    return redirect('item_list')





####################### CATEGORY VIEW #########################
@is_authenticated
def category_create(request):
    user=User.objects.get(id=request.session['pk'])
    form = CategoryForm(request.POST,request.FILES)
    if request.method == "POST":
        sec = request.POST.get('on')       
        if form.is_valid():
            section=form.save(commit=False)
            section.created_user=user
            section.created_date= datetime.today()
            if sec == 'on':
                section.status=True
                section.save()
            else:
                section.status=False
                section.save()
            return redirect('category_list')
    item = Item.objects.all()
    return render(request, 'Category/category-create.html', {'form':form,'item':item})

@is_authenticated
def category_view(request, pk):
    book= get_object_or_404(Category, pk=pk)    
    return render(request, 'Category/category-detail.html', {'loki':book})

@is_authenticated
def category_list(request):
    form =Category.objects.all()
    return render(request,'Category/category-list.html',{'form':form})

@is_authenticated
def category_edit(request,pk):
    book = get_object_or_404(Category,pk=pk)
    user=User.objects.get(id=request.session['pk'])
    form=CategoryForm(instance=book)    
    if request.method == "POST":
        lis=request.POST.getlist('item')
        book.item.clear()
        for x in lis:
            book.item.add(Item.objects.get(id=int(x)))
            book.save()
        sec = request.POST.get('on')       
        form=CategoryForm(request.POST,request.FILES,instance=book)       
        if form.is_valid():
            section=form.save(commit=False)
            section.modified_user=user
            section.modified_date=datetime.today()
            if sec == 'on':
                section.status=True
                section.save()
            else:
                section.status=False
                section.save()
            return redirect('category_list')
    item=Item.objects.all()   
    return render(request,'Category/category-create.html',{'form':form,'book':book,'item':item})

@is_authenticated
def category_delete(request,pk):
    form=Category.objects.get(pk=pk)
    form.delete()
    return redirect('category_list')

@is_authenticated
def contact(request):
    return render(request, {})





#################################  HOME SECTIION 1 #########################
@is_authenticated
def sec1_create(request):
    book = Section1.objects.first()
    user=User.objects.get(id=request.session['pk'])
    form = Sec1Form(request.POST,request.FILES,instance=book)
    if request.method == "POST":
        form = Sec1Form(request.POST,request.FILES,instance=book)
        sec = request.POST.get('on')       
        if form.is_valid():
            section=form.save(commit=False)
            section.created_user=user
            section.created_date= datetime.today()
            if sec == 'on':
                section.status=True
                section.save()
            else:
                section.status=False
                section.save()
            return redirect('sec1_list')
    return render(request, 'Section1/sec1-create.html', {'form':form})

@is_authenticated
def sec1_view(request, pk):
    book= get_object_or_404(Section1, pk=pk)    
    return render(request, 'Section1/sec1-view.html', {'loki':book})

@is_authenticated
def sec1_list(request):
    form =Section1.objects.all()
    return render(request,'Section1/sec1-list.html',{'form':form})

@is_authenticated
def sec1_edit(request,pk):
    book = Section1.objects.first()
    user=User.objects.get(id=request.session['pk'])
    form=Sec1Form(instance=book)    
    if request.method == "POST":
        sec = request.POST.get('on')       
        form=Sec1Form(request.POST,request.FILES,instance=book)       
        if form.is_valid():
            section=form.save(commit=False)
            section.modified_user=user
            section.modified_date=datetime.today()
            if sec == 'on':
                section.status=True
                section.save()
            else:
                section.status=False
                section.save()
        return redirect('sec1_list')    
    return render(request,'Section1/sec1-create.html',{'form':form,'book':book})

@is_authenticated    
def sec1_delete(request,pk):
    form=Section1.objects.get(pk=pk)
    form.delete()
    return redirect('sec1_list')




#################################  HOME SECTIION 2 #########################


@is_authenticated
def sec2_create(request):
    book = Section2.objects.first()
    user=User.objects.get(id=request.session['pk'])
    form = Sec2Form(request.POST,request.FILES,instance=book)
    if request.method == "POST": 
        form = Sec2Form(request.POST,request.FILES,instance=book)
        sec = request.POST.get('on')             
        if form.is_valid():
            section=form.save(commit=False)
            section.created_user=user
            section.created_date= datetime.today()
            if sec == 'on':
                section.status=True
                section.save()
            else:
                section.status=False
                section.save()
            return redirect('sec2_list')
    return render(request, 'Section2/sec2-create.html', {'form':form})

@is_authenticated
def sec2_view(request, pk):
    book= get_object_or_404(Section2, pk=pk)    
    return render(request, 'Section1/sec2-view.html', {'loki':book})

@is_authenticated   
def sec2_list(request):
    form =Section2.objects.all()
    return render(request,'Section2/sec2-list.html',{'form':form})

@is_authenticated
def sec2_edit(request,pk):
    book = Section2.objects.first()
    user=User.objects.get(id=request.session['pk'])
    form=Sec2Form(instance=book)    
    if request.method == "POST":
        sec = request.POST.get('on')       
        form=Sec2Form(request.POST,request.FILES,instance=book)       
        if form.is_valid():
            section=form.save(commit=False)
            section.modified_user=user
            section.modified_date=datetime.today()
            if sec == 'on':
                section.status=True
                section.save()
            else:
                section.status=False
                section.save()
            return redirect('sec2_list')    
    return render(request,'Section2/sec2-create.html',{'form':form,'book':book})

@is_authenticated
def sec2_delete(request,pk):
    form=Section2.objects.get(pk=pk)
    form.delete()
    return redirect('sec2_list')




#################################  Why Us #########################

@is_authenticated
def whyus_create(request):
    user=User.objects.get(id=request.session['pk'])
    form = ItemForm(request.POST,request.FILES)
    if request.method == "POST":
        sec = request.POST.get('on')       
        if form.is_valid():
            section=form.save(commit=False)
            section.created_user=user
            section.created_date= datetime.today()
            if sec == 'on':
                section.status=True
                section.save()
            else:
                section.status=False
                section.save()
            return redirect('whyus_list')
    return render(request, 'WhyUs/whyus-create.html', {'form':form})

@is_authenticated
def whyus_view(request, pk):
    book= get_object_or_404(WhyUs, pk=pk)    
    return render(request, 'WhyUs/whyus-view.html', {'loki':book})

@is_authenticated
def whyus_list(request):
    form =WhyUs.objects.all()
    return render(request,'WhyUs/whyus-list.html',{'form':form})

@is_authenticated
def whyus_edit(request,pk):
    book = get_object_or_404(WhyUs,pk=pk)
    user=User.objects.get(id=request.session['pk'])
    form=WhyUsForm(instance=book)    
    if request.method == "POST":
        sec = request.POST.get('on')       
        form=WhyUsForm(request.POST,request.FILES,instance=book)       
        if form.is_valid():
            section=form.save(commit=False)
            section.modified_user=user
            section.modified_date=datetime.today()
            if sec == 'on':
                section.status=True
                section.save()
            else:
                section.status=False
                section.save()
            return redirect('whyus_list')    
    return render(request,'WhyUs/whyus-create.html',{'form':form,'book':book})

@is_authenticated
def whyus_delete(request,pk):
    form=WhyUs.objects.get(pk=pk)
    form.delete()
    return redirect('whyus_list')


#################################  Our TEAM #########################

@is_authenticated
def ourteam_create(request):
    user=User.objects.get(id=request.session['pk'])
    form = OurteamForm(request.POST,request.FILES)
    if request.method == "POST":
        sec = request.POST.get('on')       
        if form.is_valid():
            section=form.save(commit=False)
            section.created_user=user
            section.created_date= datetime.today()
            if sec == 'on':
                section.status=True
                section.save()
            else:
                section.status=False
                section.save()
            return redirect('ourteam_list')
    return render(request, 'OurTeam/ourteam-create.html', {'form':form})

@is_authenticated
def ourteam_view(request, pk):
    book= get_object_or_404(Ourteam, pk=pk)    
    return render(request, 'Ourteam/ourteam-view.html', {'loki':book})

@is_authenticated
def ourteam_list(request):
    form =Ourteam.objects.all()
    return render(request,'OurTeam/ourteam-list.html',{'form':form})

@is_authenticated
def ourteam_edit(request,pk):
    book = get_object_or_404(Ourteam,pk=pk)
    user=User.objects.get(id=request.session['pk'])
    form=OurteamForm(instance=book)    
    if request.method == "POST":
        sec = request.POST.get('on')       
        form=OurteamForm(request.POST,request.FILES,instance=book)       
        if form.is_valid():
            section=form.save(commit=False)
            section.modified_user=user
            section.modified_date=datetime.today()
            if sec == 'on':
                section.status=True
                section.save()
            else:
                section.status=False
                section.save()
            return redirect('ourteam_list')    
    return render(request,'OurTeam/ourteam-create.html',{'form':form,'book':book})

@is_authenticated
def ourteam_delete(request,pk):
    form=Ourteam.objects.get(pk=pk)
    form.delete()
    return redirect('ourteam_list')



#################################  Specialities #########################

@is_authenticated
def specialities_create(request):
    user=User.objects.get(id=request.session['pk'])
    form = SpecialitiesForm(request.POST,request.FILES)
    if request.method == "POST":
        sec = request.POST.get('on')       
        if form.is_valid():
            section=form.save(commit=False)
            section.created_user=user
            section.created_date= datetime.today()
            if sec == 'on':
                section.status=True
                section.save()
            else:
                section.status=False
                section.save()
            return redirect('specialities_list')
    return render(request, 'Specialities/specialities-create.html', {'form':form})

@is_authenticated
def specialities_list(request):
    form =Specialities.objects.all()
    return render(request,'Specialities/specialities-list.html',{'form':form})

@is_authenticated
def specialities_view(request, pk):
    book= get_object_or_404(Specialities, pk=pk)    
    return render(request, 'Specialities/specialities-view.html', {'loki':book})

@is_authenticated
def specialities_edit(request,pk):
    book = get_object_or_404(Specialities,pk=pk)
    user=User.objects.get(id=request.session['pk'])
    form=SpecialitiesForm(instance=book)    
    if request.method == "POST":
        sec = request.POST.get('on')       
        form=SpecialitiesForm(request.POST,request.FILES,instance=book)       
        if form.is_valid():
            section=form.save(commit=False)
            section.modified_user=user
            section.modified_date=datetime.today()
            if sec == 'on':
                section.status=True
                section.save()
            else:
                section.status=False
                section.save()
            return redirect('specialities_list')    
    return render(request,'Specialities/specialities-create.html',{'form':form,'book':book})

@is_authenticated
def specialities_delete(request,pk):
    form=Specialities.objects.get(pk=pk)
    form.delete()
    return redirect('specialities_list')




################################# Procedure #########################

@is_authenticated
def procedure_create(request):
    user=User.objects.get(id=request.session['pk'])
    form = ProceduerForm(request.POST,request.FILES)
    if request.method == "POST":
        sec = request.POST.get('on')       
        if form.is_valid():
            section=form.save(commit=False)
            section.created_user=user
            section.created_date= datetime.today()
            if sec == 'on':
                section.status=True
                section.save()
            else:
                section.status=False
                section.save()
            return redirect('procedure_list')
    return render(request, 'Procedure/procedure-create.html', {'form':form})



@is_authenticated
def procedure_list(request):
    form =Procedure.objects.all()
    return render(request,'Procedure/procedure-list.html',{'form':form})

@is_authenticated
def procedure_view(request, pk):
    book= get_object_or_404(Procedure, pk=pk)    
    return render(request, 'Procedure/procedure-view.html', {'loki':book})

@is_authenticated
def procedure_edit(request,pk):
    book = get_object_or_404(Procedure,pk=pk)
    user=User.objects.get(id=request.session['pk'])
    form=ProceduerForm(instance=book)    
    if request.method == "POST":
        sec = request.POST.get('on')       
        form=ProceduerForm(request.POST,request.FILES,instance=book)       
        if form.is_valid():
            section=form.save(commit=False)
            section.modified_user=user
            section.modified_date=datetime.today()
            if sec == 'on':
                section.status=True
                section.save()
            else:
                section.status=False
                section.save()
            return redirect('procedure_list')    
    return render(request,'Procedure/procedure-create.html',{'form':form,'book':book})

@is_authenticated
def procedure_delete(request,pk):
    form=Procedure.objects.get(pk=pk)
    form.delete()
    return redirect('procedure_list')



################################# Event #########################


@is_authenticated
def event_create(request):
    user=User.objects.get(id=request.session['pk'])
    form = EventForm(request.POST,request.FILES)
    if request.method == "POST":
        sec = request.POST.get('on')       
        if form.is_valid():
            section=form.save(commit=False)
            section.created_user=user
            section.created_date= datetime.today()
            if sec == 'on':
                section.status=True
                section.save()
            else:
                section.status=False
                section.save()
            return redirect('event_list')
    return render(request, 'Event/event-create.html', {'form':form})

@is_authenticated
def event_list(request):
    form =Event.objects.all()
    return render(request,'Event/event-list.html',{'form':form})

@is_authenticated
def event_view(request, pk):
    book= get_object_or_404(Event, pk=pk)    
    return render(request, 'Event/event-view.html', {'loki':book})


@is_authenticated
def event_edit(request,pk):
    book = get_object_or_404(Event,pk=pk)
    user=User.objects.get(id=request.session['pk'])
    form=EventForm(instance=book)    
    if request.method == "POST":
        sec = request.POST.get('on')       
        form=EventForm(request.POST,request.FILES,instance=book)       
        if form.is_valid():
            section=form.save(commit=False)
            section.modified_user=user
            section.modified_date=datetime.today()
            if sec == 'on':
                section.status=True
                section.save()
            else:
                section.status=False
                section.save()
            return redirect('event_list')    
    return render(request,'Event/event-create.html',{'form':form,'book':book})

@is_authenticated    
def event_delete(request,pk):
    form=Event.objects.get(pk=pk)
    form.delete()
    return redirect('event_list')



################################# Images #########################


@is_authenticated
def image_create(request):
    user=User.objects.get(id=request.session['pk'])
    form = ImageForm(request.POST,request.FILES)
    if request.method == "POST":
        sec = request.POST.get('on')       
        if form.is_valid():
            section=form.save(commit=False)
            section.created_user=user
            section.created_date= datetime.today()
            if sec == 'on':
                section.status=True
                section.save()
            else:
                section.status=False
                section.save()
            return redirect('image_list')
    event = Event.objects.all()        
    return render(request, 'Images/image-create.html', {'form':form,'event':event})

@is_authenticated
def image_list(request):
    form =Images.objects.all()
    return render(request,'Images/image-list.html',{'form':form})

@is_authenticated
def image_view(request, pk):
    book= get_object_or_404(Images, pk=pk)    
    return render(request, 'Images/image-view.html', {'loki':book})

@is_authenticated
def image_edit(request,pk):
    book = get_object_or_404(Images,pk=pk)
    user=User.objects.get(id=request.session['pk'])
    form=ImageForm(instance=book)    
    if request.method == "POST":
        sec = request.POST.get('on')       
        form=ImageForm(request.POST,request.FILES,instance=book)       
        if form.is_valid():
            section=form.save(commit=False)
            section.modified_user=user
            section.modified_date=datetime.today()
            if sec == 'on':
                section.status=True
                section.save()
            else:
                section.status=False
                section.save()
            return redirect('image_list')   
    event = Event.objects.all() 
    return render(request,'Images/image-create.html',{'form':form,'book':book,'event':event})
 
@is_authenticated   
def image_delete(request,pk):
    form=Images.objects.get(pk=pk)
    form.delete()
    return redirect('image_list')

