import inspect
from functools import wraps


def inject_classmethod(target_function, new_function):
    target_function = target_function.__func__

    def _inject(*args, **kwargs):
        return new_function(target_function, *args, **kwargs)

    return classmethod(_inject)


def inject_to_classmethod(target_object, target_function_name):
    def _inject_to(new_function):
        target_function = getattr(target_object, target_function_name)
        setattr(target_object, target_function_name, inject_classmethod(target_function, new_function))
        return new_function

    return _inject_to


def inject(target_object, target_function_name, safe=False):
    if safe:
        if not hasattr(target_object, target_function_name):
            def _self_wrap(wrap_function):
                return wrap_function

            return _self_wrap

    def _wrap_original_function(original_function, new_function):

        @wraps(original_function)
        def _wrapped_function(*args, **kwargs):
            if type(original_function) is property:
                return new_function(original_function.fget, *args, **kwargs)
            return new_function(original_function, *args, **kwargs)

        if inspect.ismethod(original_function):
            return classmethod(_wrapped_function)
        if type(original_function) is property:
            return property(_wrapped_function)
        return _wrapped_function

    def _injected(wrap_function):
        original_function = getattr(target_object, target_function_name)
        setattr(target_object, target_function_name, _wrap_original_function(original_function, wrap_function))
        return wrap_function

    return _injected