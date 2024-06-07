from django.shortcuts import redirect
from functools import wraps

def session_login_required(function=None):
    def decorator(view_func):
        @wraps(view_func)
        def f(request,*args,**kwargs):
            if request.session.get('username'):
                return view_func(request, *args, **kwargs)
            return redirect('loginform')
        return f
    if function is not None:
        return decorator(function)
    return decorator