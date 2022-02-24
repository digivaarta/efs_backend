from django.utils.decorators import method_decorator
from django.http import HttpResponseBadRequest
from django.core.exceptions import PermissionDenied
from functools import wraps


def class_decorator(decorator):
    def inner(cls):
        orig_dispatch = cls.dispatch
        @method_decorator(decorator)
        def new_dispatch(self, request, *args, **kwargs):
            return orig_dispatch(self, request, *args, **kwargs)
        cls.dispatch = new_dispatch
        return cls
    return inner

def ajax_required(f):
    def wrap(request, *args, **kwargs):
            if not request.is_ajax():
                return HttpResponseBadRequest()
            return f(request, *args, **kwargs)
    wrap.__doc__=f.__doc__
    wrap.__name__=f.__name__
    return wrap

def require_ajax(view):
    @wraps(view)
    def _wrapped_view(request, *args, **kwargs):
        if request.is_ajax():
            return view(request, *args, **kwargs)
        else:
            raise PermissionDenied()
    return _wrapped_view
