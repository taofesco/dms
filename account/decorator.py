from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


def admin_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='staff'):
    '''
    Decorator for views that checks that the logged in user is a staff,
    redirects to the log-in page if necessary.
    '''
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_admin,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def staff_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None):
    '''
    Decorator for views that checks that the logged in user is a patient,
    redirects to the log-in page if necessary.
    '''
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_doctor,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def admin_only(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_admin and request.user.is_active:
            return function(request, *args, **kwargs)
        if request.user.is_active and request.user.is_staff:
            return redirect('staff')
        if request.user.is_active and request.user.is_patient:
            return redirect('patient')
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap





def allowed_user(allowed_users=[]):
    def decorator(function):
        def wrap(request, *args, **kwargs):
            user = str(request.user)
            if user in allowed_users:
                return function(request, *args, **kwargs)
            else:
                return render(request, "error/403.html")
        return wrap
    return decorator
