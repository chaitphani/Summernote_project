from NJnaiduapp.models import User
from django.shortcuts import render, redirect

def is_authenticated(f):
        def wrap(request, *args, **kwargs):
                #this check the session if userid key exist, if not it will redirect to login page
            try:
                user_obj = User.objects.get(id=request.session['pk'],mobile_number=request.session['mobile'])
            except:
                user_obj = False
            if 'pk' and 'mobile' in request.session.keys() and user_obj.status:
                return f(request, *args, **kwargs)
            request.session.clear()
            return redirect("login")
        wrap.__doc__=f.__doc__
        wrap.__name__=f.__name__
        return wrap
